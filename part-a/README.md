Part A: Deploying the Webhook API

1️⃣ Create the Project Directory Structure

mkdir -p sre-devops-modernized/part-a/k8s-manifests
mkdir -p sre-devops-modernized/part-a/webhook-app
mkdir -p sre-devops-modernized/part-a/.github/workflows
cd sre-devops-modernized

2️⃣ Write the Webhook API in Python

Create the file part-a/webhook-app/main.py:

from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

DISCORD_WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")

@app.route("/", methods=["GET"])
def health_check():
    return jsonify({"status": "ok"}), 200

@app.route("/webhook", methods=["POST"])
def handle_webhook():
    data = request.json
    commit_sha = data.get("head_commit", {}).get("id", "unknown")

    message = f"New commit pushed: {commit_sha}"
    payload = {"content": message}

    if DISCORD_WEBHOOK_URL:
        requests.post(DISCORD_WEBHOOK_URL, json=payload)

    return jsonify({"status": "message sent", "commit_sha": commit_sha}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

3️⃣ Define Dependencies

Create the file part-a/webhook-app/requirements.txt:

echo "flask\nrequests" > part-a/webhook-app/requirements.txt

4️⃣ Create Kubernetes Manifests

🔹 Kubernetes Deployment & Service

Create the file part-a/k8s-manifests/webhook-app.yaml:

apiVersion: apps/v1
kind: Deployment
metadata:
  name: webhook-api
  labels:
    app: webhook-api
spec:
  replicas: 1
  selector:
    matchLabels:
      app: webhook-api
  template:
    metadata:
      labels:
        app: webhook-api
    spec:
      containers:
      - name: webhook-api
        image: ghcr.io/YOUR_GITHUB_USERNAME/webhook-api:latest
        imagePullPolicy: Always
        ports:
        - containerPort: 5000
        env:
        - name: DISCORD_WEBHOOK_URL
          valueFrom:
            secretKeyRef:
              name: discord-webhook
              key: url
---
apiVersion: v1
kind: Service
metadata:
  name: webhook-api
spec:
  selector:
    app: webhook-api
  ports:
  - protocol: TCP
    port: 80
    targetPort: 5000
  type: ClusterIP

🔹 Kubernetes Secret for Discord Webhook

Create the file part-a/k8s-manifests/discord-webhook-secret.yaml:

apiVersion: v1
kind: Secret
metadata:
  name: discord-webhook
type: Opaque
stringData:
  url: "$(DISCORD_WEBHOOK_URL)"

5️⃣ Push Docker Image to GitHub Container Registry (GHCR)

Build and push the Docker image to GHCR:

docker build -t ghcr.io/YOUR_GITHUB_USERNAME/webhook-api:latest part-a/webhook-app/
docker push ghcr.io/YOUR_GITHUB_USERNAME/webhook-api:latest

6️⃣ Deploy to Kubernetes Using GHCR

Run the following commands to apply the manifests:

kubectl apply -f part-a/k8s-manifests/discord-webhook-secret.yaml
kubectl apply -f part-a/k8s-manifests/webhook-app.yaml

Verify deployment:
kubectl get pods
kubectl get svc

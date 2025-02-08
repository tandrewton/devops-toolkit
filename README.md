# DevOps Toolkit

## Overview

- **Git as the Source of Truth:** All Kubernetes configurations are managed via Git, ensuring consistent deployments.
- **Automated CI/CD Pipeline:** GitHub Actions builds and pushes containerized applications to GitHub Container Registry (GHCR).
- **GitOps with ArgoCD:** ArgoCD continuously syncs Kubernetes state with the Git repository, ensuring deployments are always up to date and self-healing if they drift.
- **Event-Driven Autoscaling:** KEDA scales the application dynamically based on webhook traffic.
- **Comprehensive Monitoring:** Prometheus and Grafana track API performance, errors, and Kubernetes resource usage.
- **Increased Developer Velocity:** Engineers can deploy by simply pushing code to Git, eliminating manual intervention.


---

## Repository Structure

```
devops-toolkit/
│── part-a/
│   ├── k8s-manifests/
│   │   ├── webhook-app.yaml   # Kubernetes Deployment & Service
│   │   ├── discord-webhook-secret.yaml  # Secret for Discord Webhook
│   ├── webhook-app/
│   │   ├── Dockerfile   # Containerization
│   │   ├── main.py   # Webhook API (Python)
│   │   ├── requirements.txt   # Dependencies
│   ├── .github/workflows/
│   │   ├── build-and-deploy.yaml   # CI/CD
│   ├── README.md
│
│── part-b/
│   ├── monitoring/
│   │   ├── opentelemetry-collector-config.yaml
│   │   ├── grafana-dashboard.json
│   │   ├── service-monitor.yaml
│   ├── autoscaling/
│   │   ├── keda-scaledobject.yaml
│   │   ├── keda-trigger.yaml
│   ├── README.md
│
└── README.md (Project overview)
```

---
## Key Features

### **1️⃣ GitOps with ArgoCD**
- **Automatic Syncing:** ArgoCD watches GitHub for changes and applies them automatically.
- **Self-Healing:** If someone manually modifies the cluster, ArgoCD resets it to match Git.
- **Rollback & History:** Roll back to previous versions in case of failures.
- **Standardized Deployments:** Ensures all environments (dev, staging, prod) use the same configuration.

### **2️⃣ Fully Automated CI/CD Pipeline**
- **GitHub Actions triggers on new commits**
- **Builds Docker images & pushes them to GHCR**
- **ArgoCD auto-deploys the latest version**

### **3️⃣ Monitoring & Observability**
- **Prometheus scrapes key performance metrics** from the Webhook API
- **Grafana visualizes system health and API performance**
- **Logs & Alerts enable proactive debugging**

### **4️⃣ Event-Driven Autoscaling with KEDA**
- **Dynamically adjusts the number of running pods** based on webhook traffic
- **Efficient resource usage** (scales up on high load, scales down when idle)

## How It Works

1️⃣ **Developer pushes code** → GitHub Actions builds & pushes a container to GHCR.  
2️⃣ **ArgoCD auto-syncs** → It detects the Git change and deploys the update.  
3️⃣ **Webhook API runs on Kubernetes**, automatically scaling when needed.  
4️⃣ **Prometheus & Grafana track performance** and visualize API health. 


## Getting Started

### Prerequisites
Before setting up this project, ensure you have the following installed:
- **Docker** (for containerization)
- **Kubernetes (kubectl & minikube/kind)**
- **Helm** (for Prometheus & Grafana setup)
- **ArgoCD CLI** (for GitOps deployments)
- **GitHub CLI** (for managing GitHub Actions)
- **KEDA CLI** (for event-driven autoscaling)
- **Discord Webhook URL** (for notifications)

### Setup Steps
1. **Clone the repository**
   ```sh
   git clone https://github.com/tandrewton/devops-toolkit.git
   cd devops-toolkit
   ```

2. **Deploy Kubernetes Applications**
   ```sh
   kubectl apply -f part-a/k8s-manifests/
   ```

3. **Set Up GitHub Actions for CI/CD**
   - Add necessary secrets to GitHub repository:
     ```plaintext
     GHCR_USERNAME=<your-github-username>
     GHCR_TOKEN=<your-github-token>
     DISCORD_WEBHOOK_URL=<your-slack-webhook-url>
     ```
   - Modify `.github/workflows/build-and-deploy.yaml` with your settings.

4. **Deploy Webhook API with ArgoCD**
   ```sh
   argocd app create webhook-api --repo <your-repo-url> --path part-a/webhook-app --dest-namespace default --dest-server https://kubernetes.default.svc
   argocd app sync webhook-api
   ```

5. **Deploy Monitoring Stack**
   ```sh
   helm install monitoring part-b/monitoring --values part-b/monitoring/values.yaml
   ```

6. **Enable Autoscaling with KEDA**
   ```sh
   kubectl apply -f part-b/autoscaling/keda-scaledobject.yaml
   ```

7. **Access Grafana Dashboard**
   ```sh
   kubectl port-forward svc/grafana 3000:80
   ```
   Open `http://localhost:3000` in your browser (default login: `admin/admin`).

---

## Features

- **Automated CI/CD** using **GitHub Actions** to deploy applications.
- **GitOps Workflow** with **ArgoCD** for seamless Kubernetes deployments.
- **Discord Notifications** for webhook events.
- **Monitoring & Logging** using **Prometheus, OpenTelemetry, and Grafana**.
- **Event-driven Autoscaling** via **KEDA**.

---

## Contributions

Contributions are welcome! Please open an issue or submit a pull request.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


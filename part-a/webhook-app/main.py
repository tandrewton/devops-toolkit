import json
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
    try:
        data = request.json
        print("Received Webhook:", json.dumps(data, indent=2))  # Log incoming request

        commit_sha = data.get("head_commit", {}).get("id", "unknown")
        if commit_sha == "unknown":
            print("Error: No valid commit SHA found.")

        message = f"New commit pushed: {commit_sha}"
        payload = {"content": message}

        if DISCORD_WEBHOOK_URL:
            discord_response = requests.post(DISCORD_WEBHOOK_URL, json=payload)
            print("Discord Response:", discord_response.status_code, discord_response.text)  # Log response
            return jsonify({"status": "message sent", "commit_sha": commit_sha}), 200
        else:
            return jsonify({"error": "DISCORD_WEBHOOK_URL not set"}), 500
    except Exception as e:
        print("Webhook Processing Error:", str(e))
        return jsonify({"error": "Internal Server Error"}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

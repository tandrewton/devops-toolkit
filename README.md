# DevOps Toolkit

## Overview

Using the following key DevOps concepts:

- **Kubernetes orchestration** (K8s manifests, deployments, scaling)
- **GitOps & CI/CD** (GitHub Actions, ArgoCD)
- **Event-driven automation** (Webhooks, Discord notifications)
- **Monitoring & observability** (Prometheus, OpenTelemetry, Grafana)
- **Autoscaling** (KEDA-based event-driven scaling)

---

## Repository Structure

```
devops-toolkit/
│── part-a/
│   ├── k8s-manifests/
│   │   ├── webhook-app.yaml
│   │   ├── discord-webhook-secret.yaml
│   ├── webhook-app/
│   │   ├── Dockerfile
│   │   ├── main.py (or Go/Node API)
│   │   ├── requirements.txt (if Python)
│   ├── .github/workflows/
│   │   ├── build-and-deploy.yaml
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


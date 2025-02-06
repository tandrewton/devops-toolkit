# devops-toolkit

key DevOps and SRE concepts:

Kubernetes orchestration (K8s manifests, deployments, scaling)

GitOps & CI/CD (GitHub Actions, ArgoCD)

Event-driven automation (Webhooks, Slack notifications)

Monitoring & observability (Prometheus, OpenTelemetry, Grafana)

Autoscaling (KEDA-based event-driven scaling)

devops-toolkit/
│── part-a/
│   ├── k8s-manifests/
│   │   ├── github-actions-runner.yaml
│   │   ├── argo-cd.yaml
│   │   ├── webhook-app.yaml
│   │   ├── slack-webhook-secret.yaml
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

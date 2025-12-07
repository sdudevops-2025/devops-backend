# Kubernetes Deployment Guide

## Prerequisites
- Minikube 
- Docker Desktop running
- kubectl configured

## Setup Instructions

### 1. Start Docker Desktop
Make sure Docker Desktop is running before proceeding.

### 2. Start Minikube
```bash
minikube start --driver=docker
```


### 2. Build Docker Image

For Minikube:
```bash
# Use Minikube's Docker daemon
eval $(minikube docker-env)
docker build -t quietplaces-backend:latest .
```


### 3. Apply Kubernetes Resources
```bash
kubectl apply -f k8s/configmap.yaml
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
```

### 4. Verify Deployment
```bash
# Check pods
kubectl get pods

# Check service
kubectl get svc

# Check deployment
kubectl get deployment
```

### 5. Access the Application

For Minikube:
```bash
minikube service quietplaces-service --url
```


Or use port-forward for testing:
```bash
kubectl port-forward svc/quietplaces-service 8000:8000
# Access via: http://localhost:8000
```

## Useful Commands

### View logs
```bash
kubectl logs -l app=quietplaces --tail=50 -f
```

### Scale deployment
```bash
kubectl scale deployment quietplaces-backend --replicas=3
```

### Update ConfigMap
```bash
kubectl edit configmap quietplaces-config
kubectl rollout restart deployment quietplaces-backend
```

### Delete resources
```bash
kubectl delete -f k8s/
```

### Debug pod
```bash
kubectl exec -it <pod-name> -- /bin/sh
```

## Notes
- The service is exposed on NodePort 30080
- 2 replicas are configured for high availability
- Health checks are configured on /health endpoint
- Database is SQLite (for production, use PostgreSQL with persistent volume)

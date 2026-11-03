# Todo EKS: Cloud-Native To-Do App

A Flask to-do app with add / mark-done / delete features, deployed on Amazon EKS
using GitHub Actions (OIDC) and Argo CD (GitOps).

## Run locally
    pip install -r requirements.txt
    python app.py        # open http://localhost:5000

## Run with Docker
    docker build -t todo-app .
    docker run -p 5000:5000 todo-app

## Run tests
    pytest

## Deployment flow
Developer -> GitHub -> GitHub Actions -> Docker image -> Amazon ECR ->
updated `k8s/deployment.yaml` in Git -> Argo CD -> Amazon EKS -> running app

Push to `main` -> GitHub Actions tests, builds, pushes the image to ECR and
updates `k8s/deployment.yaml` -> Argo CD syncs the change to EKS.

Submitted by: Sanika Nilesh Nikam | PRN: 20240801034

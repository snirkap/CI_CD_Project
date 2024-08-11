# CI_CD_Project
## Here you can see a diagram explaining the project:
![CI_CD_project (1)](https://github.com/user-attachments/assets/65e95bff-2e66-4dea-8980-e2fd9449aa20)


## Overview:
This project demonstrates a complete CI/CD pipeline for a Flask application using GitHub Actions, Docker, and Kubernetes with Argo CD. It includes automated building and pushing of Docker images, and seamless deployment to a Kubernetes cluster. The setup ensures a streamlined workflow for continuous integration and deployment, enhancing development efficiency and application reliability.

## Project Components:
1. **Flask Application:** A simple web application built using the Flask framework.
2. **Docker:** Containerizes the Flask application for consistent runtime environments.
3. **GitHub Actions:** Automates the CI/CD pipeline for building, testing, and deploying the application.
4. **Kubernetes:** Orchestrates the deployment, scaling, and management of the containerized application.
5. **Argo CD:** Manages continuous delivery and deployment of the application to the Kubernetes cluster.

## Requirements
1. **Docker:** To build and run the Docker container for the Flask application.
2. **Kubernetes Cluster:** To deploy and manage the application (e.g., kind, minikube, or a cloud provider).
3. **kubectl:** Kubernetes command-line tool to interact with the cluster.
4. **Argo CD:** Continuous delivery tool for Kubernetes, for managing application deployments.
5. **Python 3.10:** Required for running the Flask application locally and in the container.
6. **GitHub Account:** For repository management and GitHub Actions integration.
7. **Docker Hub Account:** To store and retrieve Docker images.

## Setup and Deployment:
### Clone the Repository:
```
git clone https://github.com/snirkap/CI_CD_Project.git
cd CI_CD_Project
```
### Set Up the Virtual Environment:
* Create and activate a Python virtual environment:
```
python3 -m venv venv
source venv/bin/activate
```
* Install dependencies:
```
pip install -r requirements.txt
```
### Build and Push Docker Image:
* Ensure you are logged in to Docker Hub:
```
docker login
```
* Build the Docker image:
```
docker build -t your-dockerhub-username/flask-app:latest .
```
* Push the Docker image to Docker Hub:
```
docker push your-dockerhub-username/flask-app:latest
```
### Set Up Kubernetes Cluster:
* Ensure your Kubernetes cluster is running and kubectl is configured to interact with it.
* Deploy Argo CD to the cluster:
```
kubectl create namespace argocd
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml
```
### Access Argo CD UI:
* Port forward the Argo CD server:
```
kubectl port-forward svc/argocd-server -n argocd 8080:443
```
* Open a web browser and navigate to https://localhost:8080.
* Log in with the default username admin and retrieve the password:
```
kubectl -n argocd get secret argocd-initial-admin-secret -o jsonpath="{.data.password}" | base64 -d
```

### Deploy the Application via Argo CD:
* In the Argo CD web UI, create a new application with the following settings:
* Application Name: flask-app
* Project: default
* Sync Policy: Automatic
* Repository URL: https://github.com/snirkap/CI_CD_Project
* Revision: master
* Path: k8s
* Cluster URL: https://kubernetes.default.svc
* Namespace: default
* Click **Create** and then **Sync** to deploy the application.

### Port Forward the Flask Application:
* Forward a local port to the service port of your Flask application:
```
kubectl port-forward svc/flask-app 8081:80
```
### Access the Flask Application:
* Open your web browser and navigate to **http://localhost:8081** to view the running Flask application.

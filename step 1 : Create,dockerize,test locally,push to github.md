# 3-Tier Attendance Nano App

## Overview

This particular application is built for knowledge-sharing purposes. We have intentionally created a very lightweight version of a 3-tier application to demonstrate the fundamentals of application deployment and containerization.

The application is a simple Attendance Management System that allows users to mark attendance through a frontend application. The frontend communicates with a Flask backend API, which in turn stores the data in a PostgreSQL database.

### Technology Stack

- Frontend: React
- Backend: Flask (Python)
- Database: PostgreSQL
- Containerization: Docker & Docker Compose

### Purpose of the Application

The primary objective of this application is to demonstrate:

- Building a simple 3-tier application
- Running the application locally using Docker
- Validating application functionality
- Understanding frontend, backend, and database interactions
- Pushing source code to GitHub
- Preparing the application for deployment to Kubernetes

This application contains only a minimal set of functionalities and is not intended for production use. It is designed purely for learning and practice purposes.

### GitHub Repository

You can find the source code here:

**Repository:**  
`https://github.com/bharathi-39/3-Tier-attendance-nano-app-`

### Deployment Approaches

Once the application is tested locally, there are multiple ways to move it to a cloud environment:

- Push the code to GitHub and clone it on an AWS EC2 instance
- Push the code to GitHub and use CI/CD pipelines
- Copy the application directly to a server using tools like WinSCP
- Deploy the containerized application to Kubernetes

This document walks through the process from local testing to source control.

---

# Build, Test Locally with Docker, and Push to GitHub

## 1. Generate the Application

A generative AI tool was used to build a lightweight Attendance Management application.

The application consists of:

- React Frontend
- Flask Backend
- PostgreSQL Database

Required dependencies were installed locally to validate functionality before deployment.

---

## 2. Run the Application Locally with Docker

The easiest way to test a multi-tier application locally is by containerizing it.

Docker Compose starts all services together:

- Frontend
- Backend
- PostgreSQL Database

### Command

```bash
docker compose up -d
```
<img width="1096" height="516" alt="image" src="https://github.com/user-attachments/assets/dedfccce-4113-4c17-b4aa-c05917971444" />

---

## 3. Check Containers and Verify the Backend

Verify that all containers are running successfully.

### Command

```bash
docker ps
```

Expected containers:

```text
frontend
backend
postgres
```

### Verify Backend API

```bash
curl http://localhost:5000/attendance
```

Expected response:

```json
[]
```

This confirms that the backend API is reachable.

---

## 4. Test the Backend from the CLI

Before testing through the frontend, validate the backend directly.

### Command (PowerShell)

```powershell
Invoke-RestMethod -Uri "http://localhost:5000/attendance" -Method Get
```
<img width="1157" height="690" alt="image" src="https://github.com/user-attachments/assets/7001ffef-dddd-4264-ad7d-59c06582dd98" />
<img width="1032" height="745" alt="image" src="https://github.com/user-attachments/assets/8131a196-7ce2-4fd8-bbf1-de962ada3d15" />


Expected Output:

```json
[]
```

---

## 5. Verify Data in PostgreSQL

Connect to the PostgreSQL container and verify that records are stored successfully.

### Command

```bash
docker exec -it nanoversion-postgres-1 psql -U postgres attendance
```

> Tip: Use the exact container name obtained from `docker ps`.

### Check Tables

```sql
\dt
```

### View Attendance Records

```sql
SELECT * FROM attendance;
```

---

## 6. Test the Frontend

Open the frontend application in a browser.

### URL

```text
http://localhost:3000
```

### Validation Steps

1. Enter a user name.
2. Mark attendance.
3. Verify the record appears in the UI.
4. Verify the same record exists in PostgreSQL.

This confirms end-to-end communication between:

```text
React Frontend
      ↓
 Flask Backend
      ↓
PostgreSQL Database
```
<img width="727" height="252" alt="image" src="https://github.com/user-attachments/assets/c0c12226-c6e0-4437-9b64-f9d3f1c1cfd8" />

---
<img width="777" height="401" alt="image" src="https://github.com/user-attachments/assets/0546457b-d459-41b6-b06d-484a71fb0bed" />

## 7. Push the Code to GitHub

Once the application is working correctly, push the source code to GitHub.

This prepares the project for future CI/CD implementation and Kubernetes deployment.

### Commands

```bash
git init
```

```bash
git add .
```

```bash
git status
```

```bash
git commit -m "3 tier nano version"
```

```bash
git branch -M main
```

```bash
git remote add origin https://github.com/bharathi-39/3-Tier-attendance-nano-app-.git
```

```bash
git push -u origin main
```

---

# Architecture

```text
+--------------------+
| React Frontend     |
+---------+----------+
          |
          |
          v
+--------------------+
| Flask Backend API  |
+---------+----------+
          |
          |
          v
+--------------------+
| PostgreSQL DB      |
+--------------------+
```

---

# Summary

These are the fundamental steps required to move an application from local development to source control.

The same workflow applies regardless of whether GitHub, Bitbucket, GitLab, or another version control platform is used.

By the end of this exercise, you should be able to:

- Build a simple 3-tier application
- Containerize the application
- Run and test locally using Docker
- Validate backend APIs
- Verify database persistence
- Manage source code in GitHub

---

# Next Steps

## 1. Clone the Repository on AWS EC2

Provision an EC2 instance and clone the GitHub repository.

```bash
git clone https://github.com/bharathi-39/3-Tier-attendance-nano-app-.git
```

---

## 2. Dockerize and Run on AWS

Install Docker and Docker Compose.

Start the containers and verify functionality.

```bash
docker compose up -d
```

---

## 3. Deploy to Kubernetes

Create a Kubernetes cluster.

Possible options:

- Amazon EKS
- Azure AKS
- Minikube
- K3s

Deploy:

- Frontend Deployment
- Backend Deployment
- PostgreSQL Deployment

---

## 4. Implement CI/CD

Integrate GitHub Actions to automate:

- Build
- Test
- Docker Image Creation
- Push to Registry
- Kubernetes Deployment

---

## Learning Outcome

This project provides a hands-on introduction to:

- Docker
- Docker Compose
- React
- Flask
- PostgreSQL
- GitHub
- Kubernetes
- CI/CD

and serves as a foundation for more advanced cloud-native application deployments.

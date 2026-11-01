# Deployment Steps - 3 Tier Attendance Nano App

## Objective

Deploy a lightweight 3-tier Attendance Management Application using:

- React Frontend
- Flask Backend
- PostgreSQL Database
- Docker
- Amazon ECR
- Amazon EKS

---

# Step 1 - Build the Application

Build the frontend, backend, and database components.

Architecture:

Frontend → Backend → PostgreSQL

---

# Step 2 - Run Locally with Docker

Start all services.

```bash
docker compose up -d
```

Verify containers:

```bash
docker ps
```

Expected:

```text
frontend
backend
postgres
```

---

# Step 3 - Verify Backend

```bash
curl http://localhost:5000/attendance
```

Expected:

```json
[]
```

---

# Step 4 - Verify Database

Connect:

```bash
docker exec -it nanoversion-postgres-1 psql -U postgres attendance
```

Check:

```sql
SELECT * FROM attendance;
```

---

# Step 5 - Push Source Code to GitHub

```bash
git init
git add .
git commit -m "3 tier attendance application"
git branch -M main
git push -u origin main
```

---

# Step 6 - Push Images to Amazon ECR

Create repositories.

```bash
aws ecr create-repository --repository-name attendance-backend
```

```bash
aws ecr create-repository --repository-name attendance-frontend
```

Authenticate:

```bash
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin <account-id>.dkr.ecr.us-east-1.amazonaws.com
```

Tag images.

```bash
docker tag nanoversion-backend:latest <ecr-url>/attendance-backend:latest
```

```bash
docker tag nanoversion-frontend:latest <ecr-url>/attendance-frontend:latest
```

Push.

```bash
docker push <ecr-url>/attendance-backend:latest
```

```bash
docker push <ecr-url>/attendance-frontend:latest
```

---

# Step 7 - Create EKS Cluster

Create:

- EKS Cluster
- Worker Nodes
- Security Groups
- IAM Roles

Validate:

```bash
kubectl get nodes
```

Expected:

```text
Ready
```

---

# Step 8 - Deploy to EKS

Apply manifests.

```bash
kubectl apply -f kubernetes/
```

Verify.

```bash
kubectl get pods
```

```bash
kubectl get svc
```

---

# Step 9 - Test Application

Backend:

```text
http://<backend-loadbalancer>:5000/attendance
```

Frontend:

```text
http://<frontend-loadbalancer>:3000
```

Validate:

- Frontend loads successfully.
- Attendance submission works.
- Records are saved in PostgreSQL.

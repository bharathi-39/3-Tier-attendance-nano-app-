
# Troubleshooting and Best Practices

This document captures issues faced during implementation and how they were resolved.

---

# Issue 1 - Frontend Build Failed

## Error

```text
npm ERR! EJSONPARSE
```

## Root Cause

package.json was missing or invalid.

## Resolution

Created:

```text
package.json
public/index.html
src/index.js
```

Rebuilt image.

```bash
docker compose build --no-cache
```

---

# Issue 2 - Frontend Container Not Starting

## Symptoms

```bash
docker ps
```

showed:

```text
backend
postgres
```

Frontend container missing.

## Root Cause

React project structure incomplete.

## Resolution

Added:

```text
public/index.html
src/index.js
```

Rebuilt and restarted.

---

# Issue 3 - Backend and Database Connectivity

## Symptoms

Unable to save attendance records.

## Investigation

Checked backend logs.

```bash
docker logs backend
```

Connected to database.

```bash
SELECT * FROM attendance;
```

## Resolution

Verified environment variables.

```text
DB_HOST
DB_USER
DB_PASSWORD
```

Corrected database configuration.

---

# Issue 4 - EKS to RDS Communication Failure

## Symptoms

Backend unable to connect to PostgreSQL.

## Root Cause

EKS and RDS were created in different VPCs.

## Resolution

Created resources inside the same VPC.

Verified:

```text
VPC ID
Subnet Configuration
Route Tables
```

---

# Issue 5 - RDS Connection Refused

## Symptoms

pgAdmin unable to connect.

## Root Cause

Security Group blocked PostgreSQL traffic.

## Resolution

Added inbound rule.

```text
Port: 5432
Source: EKS Security Group
```

Verified connectivity.

---

# Issue 6 - Frontend Not Calling Backend

## Symptoms

Frontend loaded successfully.

Attendance save operation failed.

## Root Cause

React application still pointed to:

```javascript
http://localhost:5000
```

Inside browser:

localhost = user machine

not

backend service

## Resolution

Updated backend URL.

```javascript
http://<backend-elb>:5000
```

Rebuilt image.

```bash
docker build
docker push
kubectl rollout restart deployment/frontend
```

---

# Issue 7 - Load Balancer DNS Changed

## Symptoms

Application worked earlier.

Stopped working after redeployment.

## Root Cause

AWS LoadBalancer DNS changed.

Frontend was hardcoded with old backend URL.

## Resolution

Updated:

```javascript
API_URL
```

with latest LoadBalancer DNS.

Rebuilt and redeployed frontend.

---

# Issue 8 - Kubernetes Pods Not Updating

## Symptoms

Changes not visible after pushing image.

## Root Cause

Kubernetes still running old image.

## Resolution

Restart deployment.

```bash
kubectl rollout restart deployment/frontend
```

```bash
kubectl rollout restart deployment/backend
```

---

# Best Practices

## Use RDS Instead of PostgreSQL Pod

For production:

```text
React
 ↓
Flask
 ↓
Amazon RDS
```

Avoid stateful databases inside EKS unless necessary.

---

## Never Hardcode Passwords

Bad:

```yaml
password
```

Use:

```text
Kubernetes Secrets
AWS Secrets Manager
Parameter Store
```

---

## Avoid Hardcoded Backend URLs

Use:

```text
Environment Variables
ConfigMaps
Ingress
```

instead of:

```javascript
http://localhost:5000
```

---

## Use Separate Environments

Maintain:

```text
Development
Testing
Production
```

separately.

---

## Store Images in ECR

Do not deploy locally built images directly.

Recommended flow:

```text
Build
 ↓
ECR
 ↓
EKS
```

---

## Enable CI/CD

Recommended pipeline:

```text
GitHub
 ↓
GitHub Actions
 ↓
Amazon ECR
 ↓
Amazon EKS
```

---

## Monitor Application

Frequently use:

```bash
kubectl get pods
kubectl get svc
kubectl logs deployment/backend
kubectl describe pod <pod-name>
```

to troubleshoot issues quickly.

---

# Key Learnings

Throughout this project, the major troubleshooting areas were:

- Docker image build issues
- React application configuration
- Frontend to backend communication
- RDS security group configuration
- VPC networking
- LoadBalancer DNS updates
- EKS deployment validation

These are common challenges encountered in real-world Kubernetes deployments.

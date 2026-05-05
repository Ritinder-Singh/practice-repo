# =============================================================================
# Docker — Fundamentals & Patterns
# =============================================================================
# Ref: Resume — Docker used in SecondBrain, PixelPod, Linux Portfolio, Genius365
#
# CHEATSHEET — most common commands:
#   docker build -t myapp:latest .
#   docker run -p 8000:8000 --env-file .env myapp:latest
#   docker exec -it <container_id> bash
#   docker logs -f <container_id>
#   docker ps -a
#   docker image prune -f
# =============================================================================


# =============================================================================
# PATTERN 1: BASIC PYTHON (FastAPI / SecondBrain style)
# =============================================================================
# FROM python:3.12-slim
#
# WORKDIR /app
#
# # Copy requirements first for layer caching (don't bust this layer on code changes)
# COPY requirements.txt .
# RUN pip install --no-cache-dir -r requirements.txt
#
# COPY . .
#
# EXPOSE 8000
# CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]


# =============================================================================
# PATTERN 2: MULTI-STAGE BUILD (Node.js / React — PixelPod / Portfolio style)
# =============================================================================
# Stage 1: build
# FROM node:20-alpine AS builder
# WORKDIR /app
# COPY package*.json ./
# RUN npm ci --only=production
# COPY . .
# RUN npm run build
#
# Stage 2: run (slim — only production artifacts)
# FROM node:20-alpine AS runner
# WORKDIR /app
# ENV NODE_ENV=production
# COPY --from=builder /app/.next ./.next
# COPY --from=builder /app/node_modules ./node_modules
# COPY --from=builder /app/package.json ./
# EXPOSE 3000
# CMD ["node", "server.js"]
#
# Why multi-stage: final image has NO build tools, source, or devDependencies → smaller attack surface


# =============================================================================
# PATTERN 3: DISTROLESS (minimal attack surface for production)
# =============================================================================
# FROM golang:1.22 AS builder
# WORKDIR /app
# COPY go.* ./
# RUN go mod download
# COPY . .
# RUN CGO_ENABLED=0 go build -o server .
#
# FROM gcr.io/distroless/static-debian12
# COPY --from=builder /app/server /server
# EXPOSE 8080
# ENTRYPOINT ["/server"]


# =============================================================================
# PATTERN 4: RASPBERRY PI / ARM (PixelPod self-hosted)
# =============================================================================
# Use buildx for cross-platform:
#   docker buildx build --platform linux/arm64 -t pixelpod:latest .
#
# FROM --platform=linux/arm64 python:3.12-slim
# WORKDIR /app
# COPY . .
# RUN pip install -r requirements.txt
# CMD ["python", "main.py"]


# =============================================================================
# BEST PRACTICES REFERENCE
# =============================================================================
# 1. Pin base image versions: python:3.12.3-slim NOT python:latest
# 2. Non-root user:
#    RUN adduser --disabled-password --gecos '' appuser
#    USER appuser
# 3. .dockerignore (always include):
#    .git, node_modules, __pycache__, .env, *.pyc, .DS_Store
# 4. COPY vs ADD: use COPY unless you need URL fetching or tar extraction
# 5. Combine RUN commands to reduce layers:
#    RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*
# 6. HEALTHCHECK:
#    HEALTHCHECK --interval=30s --timeout=3s CMD curl -f http://localhost:8000/health || exit 1


# This file is used as a reference — actual Dockerfiles live in each project.

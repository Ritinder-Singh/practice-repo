# Node.js REST API (Express + TypeScript + Postgres)

**Roadmap:** Major Project

## Setup
```bash
npm init -y
npm install express pg dotenv zod
npm install -D typescript @types/express @types/node @types/pg ts-node nodemon
```

## TODO 1 (Mini): Products CRUD
- GET /health | GET /products (pagination) | POST /products (Zod validation)
- GET/PUT/DELETE /products/:id (404 handling, soft delete)

## TODO 2 (Intermediate): Auth + middleware
- JWT auth: POST /auth/login, POST /auth/register
- requireAuth middleware → attaches user to req.user
- Rate limiting (express-rate-limit), error handler middleware

## TODO 3 (Advanced): Production patterns
- pg Pool, connection string from env
- Database migrations (node-pg-migrate)
- Pino logging, OpenAPI spec (swagger-jsdoc)
- Graceful shutdown on SIGTERM

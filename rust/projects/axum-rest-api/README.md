# Axum REST API (Major)

**Roadmap:** Major — Async REST API with Axum + SQLx + Tokio

## Setup
```bash
cargo new axum-rest-api && cd axum-rest-api
```
Add to `Cargo.toml`:
```toml
[dependencies]
axum = "0.7"
tokio = { version = "1", features = ["full"] }
sqlx = { version = "0.7", features = ["postgres", "runtime-tokio-native-tls", "chrono"] }
serde = { version = "1", features = ["derive"] }
serde_json = "1"
tower-http = { version = "0.5", features = ["cors", "trace"] }
dotenv = "0.15"
```

## TODO 1 (Mini): Products CRUD
- `GET /products` — list (pagination)
- `POST /products` — create (JSON body, validate)
- `GET /products/:id` — 404 if not found
- `PUT /products/:id` — update
- `DELETE /products/:id` — delete

## TODO 2 (Intermediate): Auth + middleware
- JWT auth: `POST /auth/login` returns token
- `axum::middleware::from_fn(auth_middleware)` extracts user
- Request ID + tracing middleware (tower-http)

## TODO 3 (Advanced): Connection pool + graceful shutdown
- `sqlx::PgPool` with `connect_lazy`
- Migrations with `sqlx migrate`
- Graceful shutdown: `tokio::signal::ctrl_c()`
- Docker: multi-stage Dockerfile (builder + runtime)

## Run
```bash
DATABASE_URL=postgres://... cargo run
curl http://localhost:3000/products
```

## Key Concepts Demonstrated

| Concept | Where |
|---------|-------|
| Axum `Router` with typed method routing | TODO 1 — product routes |
| `tokio` async runtime (`#[tokio::main]`) | `src/main.rs` |
| `serde::Deserialize` / `Serialize` on request/response structs | request/response types |
| `sqlx::PgPool` connection pool with `connect_lazy` | TODO 3 |
| `sqlx migrate` for schema migration management | TODO 3 |
| `axum::middleware::from_fn` for auth middleware | TODO 2 |
| JWT-based authentication | TODO 2 — `POST /auth/login` |
| `tower-http` CORS + tracing layers | `Cargo.toml` |
| Graceful shutdown with `tokio::signal::ctrl_c()` | TODO 3 |
| Multi-stage Docker build (builder + runtime) | TODO 3 |

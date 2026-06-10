# FastAPI REST Service

**Roadmap:** Major Project — FastAPI + SQLAlchemy + Alembic migrations

## Setup
```bash
pip install fastapi uvicorn sqlalchemy alembic psycopg2-binary pydantic
```

## TODO 1 (Mini): Products CRUD
- `GET /products` — list (pagination: skip, limit)
- `POST /products` — create, validate with Pydantic
- `GET /products/{id}` — 404 if not found
- `PUT /products/{id}` — full update
- `DELETE /products/{id}` — soft delete (set deleted_at)

## TODO 2 (Intermediate): Auth + migrations
- Alembic migrations: `alembic init alembic`, create first migration
- User model + JWT auth (python-jose + passlib)
- `Depends(get_current_user)` to protect routes
- `POST /auth/login`, `POST /auth/register`, `GET /me`

## TODO 3 (Advanced): Testing + deployment
- pytest + TestClient with an in-memory SQLite test database
- Background tasks (send email on order)
- Docker: `FROM python:3.12-slim`, uvicorn CMD
- OpenAPI examples on schemas

## Run
```bash
uvicorn main:app --reload
# Docs at: http://localhost:8000/docs
```

## Key Concepts Demonstrated

| Concept | Where |
|---------|-------|
| Pydantic schema validation on request bodies | `schemas.py` |
| Pagination with `skip` + `limit` query parameters | TODO 1 — `GET /products` |
| Soft delete pattern (`deleted_at` timestamp column) | TODO 1 — `DELETE /products/:id` |
| Alembic database migrations (`alembic init`, `upgrade head`) | TODO 2 |
| JWT authentication with `python-jose` + `passlib` | TODO 2 |
| `Depends(get_current_user)` for route protection | TODO 2 |
| `TestClient` with in-memory SQLite for isolated tests | TODO 3 |
| FastAPI `BackgroundTasks` for async side-effects | TODO 3 |
| Multi-stage Docker image (`python:3.12-slim`) | TODO 3 |
| OpenAPI schema `examples` on Pydantic models | TODO 3 |

# User CRUD — FastAPI + SQLAlchemy

## Architecture

```
[FastAPI]  ──SQLAlchemy──►  [SQLite (dev)]
 port 8000
```

## Project Structure

```
fastapi-crud/
├── requirements.txt         # fastapi, uvicorn, sqlalchemy, pydantic
├── main.py                  # FastAPI app entry — mounts router, registers exception handlers
├── database.py              # SQLAlchemy engine, SessionLocal, Base, get_db() dependency
├── models/
│   └── user.py              # SQLAlchemy ORM model (User table)
├── schemas/
│   ├── __init__.py
│   └── user_schema.py       # Pydantic models: UserBase, UserCreate, UserUpdate, UserResponse
├── repositories/
│   └── user_repository.py   # DB queries: get, get_all, create, update, delete
├── services/
│   └── user_service.py      # Business logic — calls repository, raises exceptions
├── routers/
│   └── users.py             # APIRouter — all /users endpoints
└── exceptions/
    └── handlers.py          # HTTPException handlers (404, 422 etc.)
```

## Setup

```bash
pip install fastapi uvicorn sqlalchemy pydantic

# Or with a requirements file:
pip install -r requirements.txt

uvicorn main:app --reload   # runs on http://localhost:8000
# Auto docs at http://localhost:8000/docs
```

## API Endpoints

| Method | Path         | Description                        |
|--------|--------------|------------------------------------|
| GET    | /users       | Return all users                   |
| GET    | /users/{id}  | Return one user (404 if missing)   |
| POST   | /users       | Create user                        |
| PUT    | /users/{id}  | Update user (partial fields OK)    |
| DELETE | /users/{id}  | Delete user                        |

## What to Build

### Database (`database.py`)
- [ ] `engine` — `create_engine("sqlite:///./users.db")`
- [ ] `SessionLocal` — `sessionmaker(autocommit=False, autoflush=False, bind=engine)`
- [ ] `Base` — `declarative_base()`
- [ ] `get_db()` — dependency that yields a session and closes it after the request

### Model (`models/user.py`)
- [ ] `User` class extending `Base` — columns: `id` (Integer, PK, autoincrement), `name` (String, not null), `email` (String, unique, not null), `created_at` (DateTime, default=now)

### Schemas (`schemas/user_schema.py`)
- [ ] `UserBase` — `name: str`, `email: EmailStr`
- [ ] `UserCreate` — extends `UserBase` (POST body)
- [ ] `UserUpdate` — all fields optional: `name: str | None`, `email: str | None` (PUT body)
- [ ] `UserResponse` — extends `UserBase`, adds `id: int`, `created_at: datetime`; `model_config = ConfigDict(from_attributes=True)`

### Repository (`repositories/user_repository.py`)
- [ ] `get_all(db)` — `db.query(User).all()`
- [ ] `get_by_id(db, user_id)` — `db.query(User).filter(User.id == user_id).first()`
- [ ] `get_by_email(db, email)` — for duplicate-email checks
- [ ] `create(db, user_data)` — instantiate, `db.add()`, `db.commit()`, `db.refresh()`
- [ ] `update(db, user, data)` — apply only non-None fields, commit, refresh
- [ ] `delete(db, user)` — `db.delete()`, `db.commit()`

### Service (`services/user_service.py`)
- [ ] `get_all_users(db)` — calls repository `get_all()`
- [ ] `get_user(db, user_id)` — calls `get_by_id()`; raises `HTTPException(404)` if not found
- [ ] `create_user(db, data)` — validates no duplicate email; calls `create()`
- [ ] `update_user(db, user_id, data)` — loads user (404 if missing), calls `update()`
- [ ] `delete_user(db, user_id)` — loads user (404 if missing), calls `delete()`

### Router (`routers/users.py`)
- [ ] `router = APIRouter(prefix="/users", tags=["users"])`
- [ ] `GET /` → `get_all_users()`
- [ ] `GET /{user_id}` → `get_user()`
- [ ] `POST /` → `create_user()`, returns `status_code=201`
- [ ] `PUT /{user_id}` → `update_user()`
- [ ] `DELETE /{user_id}` → `delete_user()`, returns `status_code=204`

### Entry point (`main.py`)
- [ ] Create `FastAPI()` app
- [ ] Call `Base.metadata.create_all(bind=engine)` on startup (creates tables)
- [ ] `app.include_router(users_router)`
- [ ] Register exception handlers from `exceptions/handlers.py`

## Key Concepts Demonstrated

| Concept | Where |
|---------|-------|
| `APIRouter` with prefix and OpenAPI tags | `routers/users.py` |
| SQLAlchemy `declarative_base()` ORM model | `models/user.py` |
| `SessionLocal` + `get_db()` as a FastAPI dependency | `database.py` |
| Pydantic v2 `model_config = ConfigDict(from_attributes=True)` | `schemas/user_schema.py` |
| Optional fields for partial `PUT` updates (`UserUpdate`) | `schemas/user_schema.py` |
| Repository pattern separating DB queries from logic | `repositories/user_repository.py` |
| Service layer raising `HTTPException(404)` | `services/user_service.py` |
| `Base.metadata.create_all()` table auto-creation on startup | `main.py` |

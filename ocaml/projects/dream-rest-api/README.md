# Dream REST API — OCaml

## Setup

```bash
opam install dream ppx_deriving_yojson caqti-driver-sqlite3 caqti-lwt
```

Create `dune-project` and `bin/main.ml`:

```
(lang dune 3.0)

(executable
 (name main)
 (libraries dream ppx_deriving_yojson caqti-driver-sqlite3))
```

## What to Build

### Milestone 1 — Basic HTTP Server
- [ ] `Dream.run ~port:3000 (Dream.router [ ... ])`
- [ ] `GET /` → `Dream.html "Hello from Dream"`
- [ ] `GET /health` → `Dream.json {|{"status":"ok"}|}`

### Milestone 2 — User CRUD Routes
- [ ] Type: `type user = { id: int; name: string; email: string } [@@deriving yojson]`
- [ ] `GET /users` → `Dream.json (Yojson.Safe.to_string (users_to_yojson !users))`
- [ ] `GET /users/:id` — `Dream.param req "id"`, return user or 404
- [ ] `POST /users` — `Dream.body req` → `Yojson.Safe.from_string` → validate → insert
- [ ] `PUT /users/:id`, `DELETE /users/:id`

### Milestone 3 — Middleware
- [ ] Content-Type JSON middleware: add `Content-Type: application/json` header
- [ ] Request logging: `Dream.logger`
- [ ] Error handling: `Dream.error_handler`

### Milestone 4 — SQLite with Caqti
- [ ] Define queries using `Caqti_request.Infix` and `Caqti_type`
- [ ] `find_user : (int, user, _) Caqti_request.t`
- [ ] `insert_user : (string * string, unit, _) Caqti_request.t`
- [ ] Use `Caqti_lwt_unix.connect` in Dream route handler

## Key Concepts Demonstrated

| Concept | Where |
|---------|-------|
| `Dream.run` + `Dream.router` server setup | `bin/main.ml` |
| `Dream.param` for URL path parameter extraction | Milestone 2 |
| `[@@deriving yojson]` ppx for automatic JSON serialization | `user` type |
| `Dream.body` for reading and parsing request JSON | Milestone 2 |
| `Dream.logger` middleware for request logging | Milestone 3 |
| `Dream.error_handler` for centralised error responses | Milestone 3 |
| Caqti typed query definitions (`Caqti_request.Infix`) | Milestone 4 |
| `Caqti_lwt_unix.connect` for async DB access with Lwt | Milestone 4 |

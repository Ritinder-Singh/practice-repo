# Servant REST API — Type-Level Routing

## Setup

```bash
stack new servant-api servant
cd servant-api
# stack.yaml: add servant-server, wai, warp, aeson
stack build
```

Or with cabal:
```bash
cabal init --template=servant
cabal install servant-server warp aeson
```

## What to Build

### Milestone 1 — API Type
- [ ] Define the API type using type-level combinators:
  ```haskell
  type UserAPI =
       "users" :> Get '[JSON] [User]
  :<|> "users" :> Capture "id" Int :> Get '[JSON] User
  :<|> "users" :> ReqBody '[JSON] CreateUserRequest :> Post '[JSON] User
  :<|> "users" :> Capture "id" Int :> ReqBody '[JSON] UpdateUserRequest :> Put '[JSON] User
  :<|> "users" :> Capture "id" Int :> Delete '[JSON] NoContent
  ```

### Milestone 2 — Server Implementation
- [ ] Implement `server :: Server UserAPI` matching each endpoint
- [ ] Use `IORef [User]` for in-memory storage
- [ ] Handle errors with `throwError err404` / `err400`

### Milestone 3 — Application
- [ ] `app :: Application` using `serve (Proxy :: Proxy UserAPI) server`
- [ ] `main = run 8080 app` with Warp

### Milestone 4 — Servant Client (optional)
- [ ] Generate client functions automatically from the same API type:
  ```haskell
  getUsers :<|> getUser :<|> createUser :<|> updateUser :<|> deleteUser =
    client (Proxy :: Proxy UserAPI)
  ```
- [ ] Test with `clientEnv <- mkClientEnv manager baseUrl`

### Milestone 5 — Authentication
- [ ] Add `BasicAuth "realm" User` or `AuthProtect "jwt"` to routes
- [ ] `AuthServerData (AuthProtect "jwt") = User`
- [ ] JWT validation in auth handler

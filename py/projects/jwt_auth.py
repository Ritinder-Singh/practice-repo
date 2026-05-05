# =============================================================================
# JWT Authentication — Full Pattern
# =============================================================================
# Topics: token generation, verification, refresh tokens, FastAPI middleware,
#         password hashing, access + refresh token rotation.
# Run: python jwt_auth.py
# Ref: Resume — JWT auth (PixelPod), NextAuth v5 (Portfolio)
# =============================================================================

import hmac
import hashlib
import base64
import json
import time
import secrets
from dataclasses import dataclass
from typing import Optional

# pip install PyJWT bcrypt fastapi python-jose[cryptography] passlib[bcrypt]


# =============================================================================
# 1. JWT FROM SCRATCH (understand the structure)
# =============================================================================

def b64url_encode(data: bytes) -> str:
    return base64.urlsafe_b64encode(data).rstrip(b"=").decode()

def b64url_decode(s: str) -> bytes:
    padding = 4 - len(s) % 4
    return base64.urlsafe_b64decode(s + "=" * padding)


class SimpleJWT:
    """Manual JWT implementation to understand the internals."""

    def __init__(self, secret: str):
        self.secret = secret.encode()

    def encode(self, payload: dict, expires_in: int = 3600) -> str:
        header = {"alg": "HS256", "typ": "JWT"}
        payload = {**payload, "iat": int(time.time()), "exp": int(time.time()) + expires_in}

        header_b64 = b64url_encode(json.dumps(header).encode())
        payload_b64 = b64url_encode(json.dumps(payload).encode())
        signing_input = f"{header_b64}.{payload_b64}".encode()

        sig = hmac.new(self.secret, signing_input, hashlib.sha256).digest()
        return f"{header_b64}.{payload_b64}.{b64url_encode(sig)}"

    def decode(self, token: str) -> dict:
        parts = token.split(".")
        if len(parts) != 3:
            raise ValueError("Invalid token format")

        header_b64, payload_b64, sig_b64 = parts
        signing_input = f"{header_b64}.{payload_b64}".encode()

        expected_sig = hmac.new(self.secret, signing_input, hashlib.sha256).digest()
        if not hmac.compare_digest(b64url_decode(sig_b64), expected_sig):
            raise ValueError("Invalid signature")

        payload = json.loads(b64url_decode(payload_b64))
        if payload.get("exp", 0) < time.time():
            raise ValueError("Token expired")

        return payload


# =============================================================================
# 2. PASSWORD HASHING
# =============================================================================

def hash_password_mock(password: str) -> str:
    """
    In production use bcrypt:
        from passlib.context import CryptContext
        pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
        hashed = pwd_context.hash(password)
        valid = pwd_context.verify(password, hashed)
    """
    salt = secrets.token_hex(16)
    h = hashlib.pbkdf2_hmac("sha256", password.encode(), salt.encode(), 260_000)
    return f"pbkdf2:sha256:{salt}:{h.hex()}"


def verify_password_mock(password: str, hashed: str) -> bool:
    _, _, salt, stored_hash = hashed.split(":")
    h = hashlib.pbkdf2_hmac("sha256", password.encode(), salt.encode(), 260_000)
    return hmac.compare_digest(h.hex(), stored_hash)


# =============================================================================
# 3. ACCESS + REFRESH TOKEN PATTERN
# =============================================================================

SECRET_KEY = "super-secret-key-change-in-production"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE = 15 * 60        # 15 minutes
REFRESH_TOKEN_EXPIRE = 7 * 24 * 3600  # 7 days

jwt = SimpleJWT(SECRET_KEY)


@dataclass
class TokenPair:
    access_token: str
    refresh_token: str
    token_type: str = "bearer"
    expires_in: int = ACCESS_TOKEN_EXPIRE


def create_token_pair(user_id: int, email: str, roles: list[str]) -> TokenPair:
    access_payload = {
        "sub": str(user_id),
        "email": email,
        "roles": roles,
        "type": "access",
    }
    refresh_payload = {
        "sub": str(user_id),
        "type": "refresh",
        "jti": secrets.token_hex(16),  # JWT ID — used for revocation
    }
    return TokenPair(
        access_token=jwt.encode(access_payload, expires_in=ACCESS_TOKEN_EXPIRE),
        refresh_token=jwt.encode(refresh_payload, expires_in=REFRESH_TOKEN_EXPIRE),
    )


def refresh_access_token(refresh_token: str) -> Optional[str]:
    """Exchange valid refresh token for new access token."""
    try:
        payload = jwt.decode(refresh_token)
        if payload.get("type") != "refresh":
            raise ValueError("Not a refresh token")
        # In production: check jti not in revocation list (Redis SET)
        new_access = jwt.encode({
            "sub": payload["sub"],
            "type": "access",
            "roles": [],  # re-fetch from DB in production
        }, expires_in=ACCESS_TOKEN_EXPIRE)
        return new_access
    except ValueError:
        return None


# =============================================================================
# 4. FASTAPI MIDDLEWARE PATTERN
# =============================================================================

FASTAPI_AUTH_PATTERN = '''
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import JWTError, jwt

security = HTTPBearer()

def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id = payload.get("sub")
        if not user_id:
            raise HTTPException(status_code=401, detail="Invalid token")
        return {"user_id": user_id, "roles": payload.get("roles", [])}
    except JWTError:
        raise HTTPException(status_code=401, detail="Token invalid or expired")

def require_role(role: str):
    def checker(user = Depends(get_current_user)):
        if role not in user["roles"]:
            raise HTTPException(status_code=403, detail="Insufficient permissions")
        return user
    return checker

# Usage:
# @app.get("/admin", dependencies=[Depends(require_role("admin"))])
# @app.get("/profile")
# async def profile(user = Depends(get_current_user)): ...
'''


# =============================================================================
# 5. NEXTAUTH V5 PATTERN (from Portfolio — for interview discussion)
# =============================================================================

NEXTAUTH_PATTERN = '''
// auth.ts (NextAuth v5)
import NextAuth from "next-auth"
import Credentials from "next-auth/providers/credentials"
import { db } from "./lib/db"
import bcrypt from "bcryptjs"

export const { handlers, signIn, signOut, auth } = NextAuth({
  providers: [
    Credentials({
      async authorize(credentials) {
        const user = await db.user.findUnique({ where: { email: credentials.email } })
        if (!user || !await bcrypt.compare(credentials.password, user.password)) return null
        return { id: user.id, email: user.email, role: user.role }
      }
    })
  ],
  callbacks: {
    jwt({ token, user }) {
      if (user) { token.role = user.role; token.id = user.id }
      return token
    },
    session({ session, token }) {
      session.user.role = token.role
      session.user.id = token.id
      return session
    }
  },
  session: { strategy: "jwt" }
})

// Middleware to protect routes:
// export { auth as middleware } from "./auth"
// export const config = { matcher: ["/dashboard/:path*", "/api/protected/:path*"] }
'''


# =============================================================================
# DEMO
# =============================================================================

if __name__ == "__main__":
    print("=== JWT from Scratch ===")
    token = jwt.encode({"sub": "42", "email": "ritinder@example.com"}, expires_in=3600)
    print(f"Token (first 60 chars): {token[:60]}...")
    payload = jwt.decode(token)
    print(f"Decoded: {payload}")

    print("\n=== Password Hashing ===")
    hashed = hash_password_mock("securepassword123")
    print(f"Hashed: {hashed[:50]}...")
    print(f"Verify correct: {verify_password_mock('securepassword123', hashed)}")
    print(f"Verify wrong:   {verify_password_mock('wrongpassword', hashed)}")

    print("\n=== Access + Refresh Token Pair ===")
    tokens = create_token_pair(42, "ritinder@example.com", ["user", "admin"])
    print(f"Access token:  {tokens.access_token[:50]}...")
    print(f"Refresh token: {tokens.refresh_token[:50]}...")
    print(f"Expires in:    {tokens.expires_in}s ({tokens.expires_in // 60} min)")

    print("\n=== Token Refresh ===")
    new_access = refresh_access_token(tokens.refresh_token)
    print(f"New access token: {new_access[:50] if new_access else 'FAILED'}...")

    # TODO: Implement token revocation with Redis SET (store jti on logout)
    # TODO: Add OAuth2 providers (Google, GitHub) via NextAuth
    # TODO: Implement PKCE flow for mobile clients (PixelPod)

"""Bifurcated identity boundary: explicit dev token OR production OIDC/JWKS.

No unauthenticated customer data, no JWT algorithm confusion, no role
escalation by user-controlled headers. APEX and Wong credentials stay elsewhere.
"""
from __future__ import annotations

import hmac
import os
import re
from dataclasses import dataclass

import jwt
from jwt import PyJWKClient
from fastapi import HTTPException, Request, status


@dataclass(frozen=True)
class Identity:
    subject: str
    tenant: str
    roles: frozenset[str]


class IdentityProvider:
    def __init__(self) -> None:
        self.environment = os.environ.get("PIPEMIND_ENV", "development")
        self.dev_token = os.environ.get("PIPEMIND_DEV_TOKEN", "")
        self.issuer = os.environ.get("PIPEMIND_JWT_ISSUER", "")
        self.audience = os.environ.get("PIPEMIND_JWT_AUDIENCE", "")
        self.jwks_url = os.environ.get("PIPEMIND_JWKS_URL", "")
        if self.environment not in ("development", "production"):
            raise RuntimeError("invalid PIPEMIND_ENV")
        if self.environment == "development":
            if len(self.dev_token) < 24:
                raise RuntimeError("development requires PIPEMIND_DEV_TOKEN >= 24 characters")
            self.jwks = None
        else:
            if not (self.issuer.startswith("https://") and self.jwks_url.startswith("https://") and self.audience):
                raise RuntimeError("production requires HTTPS OIDC issuer, JWKS URL and JWT audience")
            if self.dev_token:
                raise RuntimeError("PIPEMIND_DEV_TOKEN forbidden in production")
            if os.environ.get("PIPEMIND_DB_PATH", ":memory:") == ":memory:":
                raise RuntimeError("production requires persistent PIPEMIND_DB_PATH")
            self.jwks = PyJWKClient(self.jwks_url, cache_keys=True, lifespan=300)

    def verify(self, token: str) -> Identity:
        if not token:
            raise HTTPException(status.HTTP_401_UNAUTHORIZED, "Bearer token required")
        if self.environment == "development":
            if not hmac.compare_digest(token, self.dev_token):
                raise HTTPException(status.HTTP_401_UNAUTHORIZED, "Invalid development token")
            return Identity(subject="local-researcher", tenant="demo", roles=frozenset({"admin","analyst","ingest","auditor"}))
        try:
            signing_key = self.jwks.get_signing_key_from_jwt(token)
            claims = jwt.decode(token, signing_key.key, algorithms=["RS256","ES256"],
                                audience=self.audience, issuer=self.issuer,
                                options={"require":["exp","iat","sub","iss","aud"]},
                                leeway=30)
            tenant=claims.get("tenant_id")
            subject=claims["sub"]
            raw_roles=claims.get("pipemind_roles",[])
            if not isinstance(raw_roles,list) or any(not isinstance(r,str) for r in raw_roles):
                raise ValueError("invalid roles claim")
            if not isinstance(tenant,str) or not re.fullmatch(r"[A-Za-z0-9_.-]{1,64}",tenant):
                raise ValueError("missing or invalid tenant_id")
            if not isinstance(subject,str) or not subject:
                raise ValueError("invalid subject")
            allowed={"viewer","analyst","ingest","admin","auditor"}
            return Identity(subject=subject, tenant=tenant, roles=frozenset(raw_roles)&allowed)
        except (jwt.PyJWTError, ValueError) as exc:
            raise HTTPException(status.HTTP_401_UNAUTHORIZED,"Invalid identity token") from exc

    def principal(self, request: Request) -> Identity:
        authorization=request.headers.get("Authorization","")
        prefix="Bearer "
        if not authorization.startswith(prefix) or len(authorization) > 8192:
            raise HTTPException(status.HTTP_401_UNAUTHORIZED,"Bearer token required")
        return self.verify(authorization[len(prefix):])

    def require(self, request: Request, *roles: str) -> Identity:
        ident=self.principal(request)
        if not ident.roles.intersection(roles) and "admin" not in ident.roles:
            raise HTTPException(status.HTTP_403_FORBIDDEN, "Insufficient role")
        return ident

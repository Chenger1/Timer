from typing import (
    Union,
    Tuple
)
from datetime import (
    datetime,
    timedelta,
    timezone
)

import jwt
from fastapi.security import (
    HTTPBearer,
    HTTPAuthorizationCredentials
)
from fastapi import Request

from src.core.config import Config
from src.core.exceptions import AuthError


ALGORITHM = "HS256"


def create_access_token(data: dict) -> Tuple[str, datetime]:
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=Config.ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, Config.JWT_RANDOM, algorithm=ALGORITHM), expire


def decode_jwt(token: str) -> Union[dict, None]:
    try:
        decoded_token = jwt.decode(token, Config.JWT_RANDOM, algorithms=[ALGORITHM])
        return decoded_token if decoded_token["exp"] >= int(round(datetime.utcnow().timestamp())) else None
    except Exception as e:
        return None


class JWTBearer(HTTPBearer):
    def __init__(self, auto_error: bool = True):
        super().__init__(auto_error=auto_error)

    async def __call__(self, request: Request):
        credentials: HTTPAuthorizationCredentials = await super(JWTBearer, self).__call__(request)
        if credentials:
            if not credentials.scheme == "Bearer":
                raise AuthError("Invalid authorization scheme")
            payload = decode_jwt(credentials.credentials)
            if payload is None:
                raise AuthError("Invalid authorization token")
            return payload
        else:
            raise AuthError("Invalid authorization token")

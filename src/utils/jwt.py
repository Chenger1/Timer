from datetime import (
    datetime,
    timedelta,
    timezone
)

import jwt


from src.core.config import Config


ALGORITHM = "HS256"


def create_access_token(data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=Config.ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, Config.JWT_RANDOM, algorithm=ALGORITHM)

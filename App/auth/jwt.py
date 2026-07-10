from datetime import datetime, timedelta, timezone
from jose import jwt, JWTError

from App.config import settings

class JWT:
    @staticmethod
    def create_access_token(data: dict) -> str:
        payload = data.copy()

        expire = datetime.now(timezone.utc) + timedelta(
            minutes=int(settings.ACCESS_TOKEN_EXPIRE_MINUTES)
        )

        payload.update({"exp": expire})

        token = jwt.encode(
            payload,
            settings.SECRET_KEY,
            algorithm=settings.ALGORITHM
        )

        return token

    @staticmethod
    def verify_access_token(token: str) -> dict:
        payload = jwt.decode(
            token,
            settings.SECRET_KEY,
            algorithms=[settings.ALGORITHM]
        )
        return payload
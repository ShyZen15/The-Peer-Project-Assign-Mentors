from datetime import datetime, timedelta, timezone
from jose import jwt, JWTError

from App.config import settings

class JWT:
    @staticmethod
    def create_access_token(data: dict) -> str:
        payload = data.copy()

        expire = datetime.now(timezone.utc) + timedelta(
            minutes=int(settings.expireTime)
        )

        payload.update({"exp": expire})

        token = jwt.encode(
            payload,
            settings.secret_key,
            algorithm=settings.algo
        )

        return token

    @staticmethod
    def verify_access_token(token: str) -> dict:
        payload = jwt.decode(
            token,
            settings.secret_key,
            algorithms=[settings.algo]
        )
        return payload
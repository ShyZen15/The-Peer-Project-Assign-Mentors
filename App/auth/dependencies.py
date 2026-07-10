from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

from App.auth.jwt import JWT

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/admin/login"
)

def get_current_admin(
        token: str = Depends(oauth2_scheme)
):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials.",
        headers={"WWW-Authenticate": "Bearer"}
    )

    print(token)

    payload = JWT.verify_access_token(token)
    
    if payload is None:
        raise credentials_exception
    
    username = payload.get("sub")
    role = payload.get("role")

    if username is None or role is None:
        raise credentials_exception
    
    if role != "admin":
        raise HTTPException(
            status_code=403,
            detail="You are not authorized"
        )
    
    return payload
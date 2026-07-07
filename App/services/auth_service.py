from App.repository.AdminRepo import AdminRepo
from fastapi import HTTPException
from App.auth.jwt import JWT
from App.auth.password import Password
from App.schemas.AdminLogin import AdminLogin


class AuthService:
    @staticmethod
    def login(credentials: AdminLogin):
        data = AdminRepo.getDataByUsername(credentials.username)
        if not data:
            raise HTTPException(
                status_code=401,
                detail="Invalid Credentials"
            )
        
        hash_passwd = data["password_hash"]
        passwdInput = credentials.password
        if Password.verify_password(hash_passwd, passwdInput):
            access_token = JWT.create_access_token(
                {
                    "sub": data["username"],
                    "role": data["role"]
                }
            )
        else:
            raise HTTPException(
                status_code=401,
                detail="Invalid Credentials"
            )
        return {
            "access_token": access_token,
            "token_type": "bearer"
        }


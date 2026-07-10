from App.repository.AdminRepo import AdminRepo
from fastapi import HTTPException
from App.auth.jwt import JWT
from App.auth.password import Password
from App.schemas.AdminLogin import AdminLogin
from App.schemas.AdminCreate import AdminResponse


class AuthService:
    @staticmethod
    def login(credentials: AdminLogin):
        data = AdminRepo.getDataByUsernames(credentials.username)
        if not data:
            raise HTTPException(
                status_code=401,
                detail="Invalid Credentials"
            )
        
        print(data)
        print(data.keys())
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
    
    @staticmethod
    def getAllAdmin():
        result = AdminRepo.getAll()

        if not result:
            raise HTTPException(
                status_code=404,
                detail="No admins found."
            )
        
        return result
    
    @staticmethod
    def getDataByUsername(username: str):
        result = AdminRepo.getDataByUsername(username)
        if not result:
            raise HTTPException(
                status_code=404,
                detail="No admins found"
            )
        
        return {
        "success": True,
        "Admin": result
    }

    @staticmethod
    def updatePasswordAdmin(username: str, passwordHash: str):
        pass

    @staticmethod
    def updateDataAdmin(username: str, data: dict):
        pass # going to define service for this

    @staticmethod
    def delete_admin(username: str):
        result = AdminRepo.deleteData(username)
        return{
            "success": True,
            "admin": result.data
        }
    
    @staticmethod
    def createAdmin(data : AdminResponse):
        if AdminRepo.getDataByUsername(data.username):
            raise HTTPException(
                status_code=409,
                detail="username already exists"
            )
        
        print(type(data.password))
        print(data.password)

        password_hash = Password.hash_password(data.password)

        admin_data = {
            "username": data.username,
            "discord_id": data.discord_id,
            "role": data.role,
            "email": data.email,
            "password_hash": password_hash
        }

        # Insert into database
        AdminRepo.create(admin_data)

        # Response
        return {
            "success": True,
            "message": "Admin created successfully."
        }


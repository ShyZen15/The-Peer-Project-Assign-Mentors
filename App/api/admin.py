from fastapi import APIRouter, HTTPException
from App.schemas.AdminLogin import AdminLogin
from App.schemas.AdminCreate import AdminResponse
from App.services.auth_service import AuthService
from postgrest.exceptions import APIError
from App.repository.AdminRepo import AdminRepo


router = APIRouter(
    prefix="/admin",
    tags=["admin"]
)

@router.post("/login")
async def adminLoginRequest(
    credentials: AdminLogin
):
    try:
        return AuthService.login(credentials)
    except APIError:
        raise HTTPException(
        status_code=500,
        detail="Database error."
    )

@router.get("/")
async def getAllAdmins():
    result = AdminRepo.getAll()
    return{
        "success": True,
        "mentor": result
    }

@router.get("/{username}")
async def get_data_by_username(username: str):
    result = AdminRepo.getDataByUsername(username)

    if not result:
        raise HTTPException(
            status_code=404,
            detail="Invalid Credential"
        )
    return{
        "success": True,
        "Admin": result
    }

# @router.get("/{username}/exists")
# async def existsAdmin(username: str):
#     return AdminRepo.exists(username)

@router.patch("/{username}/password")
async def updatePasswordAdmin(username: str, passwordHash: str):
    pass # going to define service for this

@router.put("/{username}")
async def updateDataAdmin(username: str, data: dict):
    pass # going to define service for this

@router.delete("/{username}")
async def delete_admin(username: str):
    result = AdminRepo.deleteData(username)
    return{
        "success": True,
        "admin": result.data
    }

@router.post("/admin")
async def createAdmin(data : AdminResponse):
    pass # going to define service for this

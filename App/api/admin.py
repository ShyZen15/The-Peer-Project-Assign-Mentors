from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordRequestForm
from App.auth.dependencies import get_current_admin
from App.schemas.AdminLogin import AdminLogin
from App.schemas.AdminCreate import AdminResponse
from App.services.auth_service import AuthService
from postgrest.exceptions import APIError
from App.repository.AdminRepo import AdminRepo


router = APIRouter(
    prefix="/admin",
    tags=["admin"]
)

#Development only
@router.post("/login")
async def adminLoginRequest(
    form_data: OAuth2PasswordRequestForm = Depends()
):
    try:
        credentials = AdminLogin(
            username=form_data.username,
            password=form_data.password
        )

        return AuthService.login(credentials)

    except APIError:
        raise HTTPException(
            status_code=500,
            detail="Database error."
        )
    
# @router.post("/login")
# async def adminLoginRequest(
#     credentials: AdminLogin
# ):
#     try:
#         return AuthService.login(credentials)

#     except APIError:
#         raise HTTPException(
#             status_code=500,
#             detail="Database error."
#         )

@router.get("/")
async def getAllAdmins(
    current_admin = Depends(get_current_admin)
):
    result = AdminRepo.getAll()
    return{
        "success": True,
        "mentor": result
    }

@router.get("/{username}")
async def get_data_by_username(
        username: str,
        current_admin = Depends(get_current_admin)
):
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

@router.delete("/{username}")
async def delete_admin(username: str, current_admin = Depends(get_current_admin)):
    result = AdminRepo.deleteData(username)
    return{
        "success": True,
        "admin": result.data
    }

@router.post("/admin")
async def createAdmin(data : AdminResponse, current_admin = Depends(get_current_admin)):
    return AuthService.createAdmin(data)

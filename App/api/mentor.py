from fastapi import APIRouter, HTTPException, Depends
from App.schemas.mentor import MentorRegistration
from App.repository.MentorRepo import MentorRepo
from postgrest.exceptions import APIError
from App.auth.dependencies import get_current_admin

router = APIRouter(
    prefix="/mentor",
    tags=["Mentor"]
)

@router.post("/")
async def register_mentor(
    mentor: MentorRegistration
): 
    
    try:
        result = MentorRepo.createData(
            mentor.model_dump(mode="json")
        )

        return {
            "success": True,
            "mentor": result.data
        }
    except APIError as e:
        if "discord_id" in str(e):
            raise HTTPException(
                status_code=409,
                detail="Discord ID already exists"
            )
        
        raise HTTPException(
            status_code=500,
            detail="Database error."
        )
    
@router.get("/count")
async def getTotal(current_admin = Depends(get_current_admin)):
    print("Endpoint reached")
    return MentorRepo.getCount()

@router.get("/mentorAll")
async def get_mentor_all(current_admin = Depends(get_current_admin)):
    print("Reached endpoint")
    print("Before repo")
    result = MentorRepo.getAll()
    print("After repo")
    print(result)
    return {
        "success": True,
        "mentor": result
    }

@router.get("/{discord_id}")
async def get_mentor_id(discord_id: str, current_admin = Depends(get_current_admin)):
    result = MentorRepo.getDataByID(discord_id)

    if not result:
        raise HTTPException(
            status_code=404,
            detail="Mentor Not Found"
        )
    return{
        "success": True,
        "mentor": result
    }

        

@router.put("/{discord_id}")
async def update_mentor_one_field(discord_id: str, data, field:str, current_admin = Depends(get_current_admin)):
    result = MentorRepo.updateDataField(discord_id, data, field)
    return{
        "success": True,
        "mentor": result.data
    }

@router.patch("/{discord_id}/verify")
async def verify_mentor(
    discord_id: str,
    is_verified: bool,
    current_admin = Depends(get_current_admin)
):
    result = MentorRepo.updateVerificationStatus(
        discord_id,
        is_verified
    )

    return {
        "success": True,
        "message": f"Verification status updated to {is_verified}",
        "mentor": result.data
    }

@router.delete("/{discord_id}/delete")
async def delete_mentor_id(discord_id: str, current_admin = Depends(get_current_admin)):
    result = MentorRepo.deleteData(discord_id)
    return{
        "success": True,
        "mentor": result.data
    }



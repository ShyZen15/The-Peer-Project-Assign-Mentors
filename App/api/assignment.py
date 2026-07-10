from fastapi import APIRouter, Depends
from App.auth.dependencies import get_current_admin
from App.schemas.assignment import Assignment
from App.repository.AssignRepo import AssignRepo

router = APIRouter(
    prefix="/Assign",
    tags=["Assign"]
)

@router.post("/")
async def assign_mentor(
    assigns: Assignment
): 
    result = AssignRepo.createData(
        assigns.model_dump(mode="json")
    )

    return {
        "success": True,
        "assign": result.data
    }

@router.get("/")
async def get_assign_all(current_admin = Depends(get_current_admin)):
    result = AssignRepo.getAll()
    return {
        "success": True,
        "assign": result
    }

@router.get("/{id}")
async def get_assign_id(id: int, current_admin = Depends(get_current_admin)):
    result = AssignRepo.getDataByID(id)
    return{
        "success": True,
        "assign": result
    }

@router.put("/{id}/moreFields")
async def update_assign_more(id: int, data:dict, current_admin = Depends(get_current_admin)):
    result = AssignRepo.updateData(id, data)
    return{
        "success": True,
        "assign": result.data
    }

@router.put("/{id}/singleField")
async def update_assign_one_field(id: int, data, field:str, current_admin = Depends(get_current_admin)):
    result = AssignRepo.updateDataField(id, data, field)
    return{
        "success": True,
        "assign": result.data
    }

@router.delete("/{id}")
async def delete_assign_id(id: int, current_admin = Depends(get_current_admin)):
    result = AssignRepo.deleteData(id)
    return{
        "success": True,
        "assign": result.data
    }

@router.get("/count")
async def getTotal(current_admin = Depends(get_current_admin)):
    return AssignRepo.getCount()

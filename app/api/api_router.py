from fastapi import APIRouter
from app.api.endpoints import task


router = APIRouter()

router.include_router(task.router, prefix="/task", tags=["task"])

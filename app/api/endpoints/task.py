from fastapi import APIRouter
from app.core.task_generator import TASK_GENERATOR


router = APIRouter()

@router.get("/generate")
async def get_task():
    task = TASK_GENERATOR.get_task()
    if task is None:
        return {
            "success": False,
            "error": "No task available"
        }
        
    return {
        "success": True,
        "html": task.html,
    }

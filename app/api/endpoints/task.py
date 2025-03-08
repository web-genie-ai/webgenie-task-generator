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


@router.get("/seed")
async def seed_task(session:int, task_number:int):
    seed = session * task_number
    return {
        "success": True,
        "seed": seed
    }
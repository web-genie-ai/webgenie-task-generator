from fastapi import APIRouter
from app.services.task import (
    get_seed, 
    get_task,
)

router = APIRouter()


@router.get("/seed")
async def seed_task(session:int, task_number:int):
    seed, task_id_seed = get_seed(session, task_number)
    return {
        "seed": seed,
        "task_id_seed": task_id_seed,
    }


@router.get("/generate")
async def generate_task(session:int, task_number:int):
    task = get_task()
    return {
        "html": task.html,
    }
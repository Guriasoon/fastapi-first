from typing import Annotated

from fastapi import APIRouter
from fastapi.params import Depends

from repository import TaskRepository
from shemas import STaskAdd, STask, StaskId

router = APIRouter(
    prefix="/task",
    tags=["Таски Хаски свагер"],
)


@router.post("")
async def add_task(task: Annotated[STaskAdd, Depends()]) -> StaskId:
    task_id = await TaskRepository.add_one(task)
    return {"ok": True, "task_id": task_id}


@router.get("")
async def get_tasks() -> list[STask]:
    tasks = await TaskRepository.find_all()
    return tasks

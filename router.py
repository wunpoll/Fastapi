from typing import Annotated

from fastapi import APIRouter, Depends

from repository import TaskRepository
from schemas import TaskAddSchema, TaskSchema, TaskIdSchema

router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"],
)


@router.get("")
async def get_tasks() -> list[TaskSchema]:
    tasks = await TaskRepository.get_all()
    return tasks

tasks = []


@router.post("")
async def add_task(
        task: Annotated[TaskAddSchema, Depends()],
) -> TaskIdSchema:
    task_id = await TaskRepository.add_one(task)

    return {"success": True, "task_id": task_id}
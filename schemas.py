from typing import Optional
from pydantic import BaseModel


class TaskAddSchema(BaseModel):
    name: str
    desc: Optional[str] = None


class TaskSchema(TaskAddSchema):
    id: int


class TaskIdSchema(BaseModel):
    success: bool = True
    task_id: int

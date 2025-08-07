from database import session, TaskModel
from schemas import TaskAddSchema, TaskSchema
from sqlalchemy import select


class TaskRepository:
    @classmethod
    async def add_one(cls, data: TaskAddSchema) -> int:
        async with session() as s:
            task_dict = data.model_dump()

            task = TaskModel(**task_dict)
            s.add(task)

            await s.flush()
            await s.commit()

            return task.id

    @classmethod
    async def get_all(cls) -> list[TaskSchema]:
        async with session() as s:
            query = select(TaskModel)
            result = await s.execute(query)
            task_models = result.scalars().all()
            task_schemas = [TaskSchema.model_validate(t) for t in task_models]
            return task_schemas

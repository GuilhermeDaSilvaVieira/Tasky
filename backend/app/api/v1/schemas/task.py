from datetime import datetime

from app.db.models.task import TaskBase


class TaskCreate(TaskBase):
    pass


class TaskUpdate(TaskBase):
    pass


class TaskResponse(TaskBase):
    id: int
    created_at: datetime
    modified_at: datetime | None

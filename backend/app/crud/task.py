from typing import Annotated
from fastapi import Query
from sqlmodel import Session, select

from app.api.v1.schemas.task import TaskCreate, TaskUpdate
from app.db.models.task import Task


def create_task(session: Session, task: TaskCreate) -> Task:
    db_task = Task.model_validate(task)
    session.add(db_task)
    session.commit()
    session.refresh(db_task)
    return db_task


def read_tasks(
    session: Session,
    offset: int = 0,
    limit: Annotated[int, Query(le=100)] = 100,
) -> list[Task]:
    return list(session.exec(select(Task).offset(offset).limit(limit)).all())


def read_task(session: Session, id: int) -> Task | None:
    return session.get(Task, id)


def read_subtasks(
    session: Session,
    parent_id: int,
    offset: int = 0,
    limit: Annotated[int, Query(le=100)] = 100,
) -> list[Task]:
    return list(
        session.exec(
            select(Task).where(Task.parent_id == parent_id).offset(offset).limit(limit)
        ).all()
    )


def update_task(session: Session, id: int, task: TaskUpdate) -> Task | None:
    db_task = session.get(Task, id)
    if db_task:
        task_data = task.model_dump(exclude_unset=True)
        db_task.sqlmodel_update(task_data)
        session.add(db_task)
        session.commit()
        session.refresh(db_task)
    return db_task


def delete_task(session: Session, id: int) -> Task | None:
    task = session.get(Task, id)
    if task:
        session.delete(task)
        session.commit()
    return task

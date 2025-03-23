from fastapi import APIRouter, HTTPException, status

from app.api.v1.schemas.task import TaskCreate, TaskResponse, TaskUpdate
from app.core.dependencies import SessionDep
from app.crud.task import create_task, delete_task, read_task, read_tasks, update_task

router = APIRouter()


@router.post("/", response_model=TaskResponse)
def create_task_endpoint(session: SessionDep, task: TaskCreate):
    return create_task(session, task)


@router.get("/", response_model=list[TaskResponse])
def read_tasks_endpoint(session: SessionDep):
    return read_tasks(session)


@router.get("/{id}", response_model=TaskResponse)
def read_task_endpoint(session: SessionDep, id: int):
    task = read_task(session, id)
    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found",
        )
    return task


@router.patch("/{id}", response_model=TaskResponse)
def update_task_endpoint(session: SessionDep, id: int, task: TaskUpdate):
    updated_task = update_task(session, id, task)
    if not updated_task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found",
        )
    return updated_task


@router.delete("/{id}", response_model=TaskResponse)
def delete_task_endpoint(session: SessionDep, id: int):
    task = delete_task(session, id)
    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found",
        )
    return task

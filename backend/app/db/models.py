from datetime import datetime
from typing import Optional
from sqlmodel import Field, Relationship, SQLModel


class TaskBase(SQLModel):
    title: str = Field(index=True)
    description: str | None = Field(default=None)
    completed: bool = Field(default=False, index=True)
    important: bool = Field(default=False, index=True)
    due_date: datetime | None = Field(default=None, index=True)
    parent_id: int | None = Field(
        default=None,
        nullable=True,
        foreign_key="task.id",
    )


class Task(TaskBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    created_at: datetime = Field(default_factory=datetime.now)
    modified_at: datetime | None = Field(
        default=None,
        sa_column_kwargs={"onupdate": datetime.now},
    )

    # SQLAlchemy is not compatible with "Task | None", it needs Optional
    parent: Optional["Task"] = Relationship(
        back_populates="children",
        sa_relationship_kwargs={
            "remote_side": "Task.id",
        },
    )
    children: list["Task"] = Relationship(
        back_populates="parent",
        cascade_delete=True,
    )

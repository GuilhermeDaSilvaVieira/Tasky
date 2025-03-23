from contextlib import asynccontextmanager
from fastapi import FastAPI

from app.db.session import init_db
from app.api.v1.endpoints import task


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield init_db()


app = FastAPI(title="Tasky API", lifespan=lifespan)

app.include_router(task.router, prefix="/api/v1/tasks", tags=["tasks"])

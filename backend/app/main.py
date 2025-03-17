from contextlib import asynccontextmanager
from fastapi import FastAPI

from app.db.session import init_db


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield init_db()


app = FastAPI(lifespan=lifespan)

from fastapi import FastAPI

from .config.db import Base 

from .config.db import engine

from .routers import events


app = FastAPI(
    title = "College Portfolio API",
    docs_url = "/documentation",
    redoc_url = None
)

Base.metadata.create_all(bind=engine)

app.include_router(events.router)
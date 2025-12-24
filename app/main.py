from fastapi import FastAPI
from app.db.base import Base
from app.db.session import engine
from app.api import events

app = FastAPI()

# Create tables on startup
@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)

app.include_router(events.router)

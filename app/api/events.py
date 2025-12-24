from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.db.models import Event, User
from app.schemas.event import EventCreate
from app.schemas.analytics import EventSummary
from sqlalchemy import func
from typing import List
from datetime import datetime

router = APIRouter(prefix="/events", tags=["events"])

# DB session dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Fake current user dependency (replace later with auth)
def get_current_user(db: Session = Depends(get_db)):
    return db.query(User).first()

@router.post("/")
def create_event(event: EventCreate, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    db_event = Event(
        user_id=user.id,
        event_type=event.event_type,
        timestamp=event.timestamp or datetime.utcnow(),
        event_metadata=event.event_metadata,
    )
    db.add(db_event)
    db.commit()
    db.refresh(db_event)
    return {"id": db_event.id}

@router.get("/summary", response_model=List[EventSummary])
def event_summary(
    start: datetime | None = None,
    end: datetime | None = None,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user)
):
    query = db.query(Event.event_type, func.count(Event.id).label("count")).filter(Event.user_id == user.id)
    if start:
        query = query.filter(Event.timestamp >= start)
    if end:
        query = query.filter(Event.timestamp <= end)
    results = query.group_by(Event.event_type).all()
    return [{"event_type": row.event_type, "count": row.count} for row in results]

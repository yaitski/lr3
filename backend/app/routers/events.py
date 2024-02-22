#import string
from tokenize import String
from fastapi import (
    APIRouter, 
    HTTPException, 
    status, 
    Depends)

from ..config.db import get_db

from ..models import Events as EventsModel

from ..schemas import BaseEvents, Event

from sqlalchemy.orm import Session
from sqlalchemy import select, insert

from typing import List

router = APIRouter(
    prefix="/api/events",
    tags=["Events"]
)

@router.post("/", response_description="Create new event", response_model=Event, status_code=status.HTTP_201_CREATED)
def create_event(work: BaseEvents, db: Session=Depends(get_db)):

    new_event = EventsModel(**work.model_dump())

    db.add(new_event)
    db.commit()
    db.refresh(new_event)

    return new_event

@router.get("/", response_description="List of all events", response_model=List[Event], status_code=status.HTTP_200_OK)
def get_all_events(db: Session=Depends(get_db)):
    events = db.query(EventsModel).all()

    if events == []:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Nothing found"
        )

    return events


@router.get("/id/", response_description="Get event by id", response_model=Event, status_code=status.HTTP_200_OK)
def get_event_by_id(id: int, db: Session=Depends(get_db)):
    event = db.query(EventsModel).filter(EventsModel.id == id).first()

    if event is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Nothing found"
        )

    return event

@router.get("/type/", response_description="Get events by type", response_model=Event, status_code=status.HTTP_200_OK)
def get_events_by_type(type: str, db: Session=Depends(get_db)):
    type_events = db.query(EventsModel).filter(EventsModel.type == type).first()

    if type_events is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Nothing found"
        )

    return type_events
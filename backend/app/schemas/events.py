from pydantic import BaseModel
from typing import Optional
from datetime import date

class BaseEvents(BaseModel):
    title: str
    date: date
    description: str
    type: str
    phone: str
    audience: int

class Event(BaseEvents):
    id: int
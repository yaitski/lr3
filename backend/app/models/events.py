from sqlalchemy import Column, Integer, String, TIMESTAMP, ForeignKey
from datetime import date as date_type

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from ..config.db import Base

class Events(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True, nullable=False)
    date = Column(TIMESTAMP, nullable=False)
    title = Column(String(50), nullable=False)
    description = Column(String(200), nullable=False)
    type = Column(String(50), nullable=False)
    phone = Column(String(50), nullable=False)
    audience = Column(Integer, nullable=False)
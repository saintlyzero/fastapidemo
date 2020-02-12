import datetime

from typing import List
from pydantic import BaseModel

from sqlalchemy import Column, Integer, String, DateTime, create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Customer(Base):
    __tablename__ = "customer"
    id = Column(Integer, primary_key = True)
    name = Column(String(255))


class Condition(Base):
    """
        Timescale DB Indexed
    """
    __tablename__ = "conditions"
    time = Column(DateTime(timezone=True), primary_key = True)
    location = Column(String)
    temperature = Column(Integer)


class Event(BaseModel):
    time: datetime.datetime
    passers: int
    staff: int
    customers: int
    camera_id: int
    store_id: int

class Events(BaseModel):
    event: List[Event]
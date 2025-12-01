from sqlalchemy import Column, Integer, String
from pydantic import BaseModel
from .db import Base

class Place(Base):
    __tablename__ = "places"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    address = Column(String, nullable=True)
    rating = Column(Integer, nullable=True)

class PlaceCreate(BaseModel):
    name: str
    address: str | None = None
    rating: int | None = None

class PlaceOut(BaseModel):
    id: int
    name: str
    address: str | None = None
    rating: int | None = None

    class Config:
        orm_mode = True

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from . import models
from .db import get_db

router = APIRouter()

@router.get('/health')
def health():
    return {'status': 'ok'}

@router.get('/places', response_model=list[models.PlaceOut])
def list_places(db: Session = Depends(get_db)):
    places = db.query(models.Place).all()
    return places

@router.post('/places', response_model=models.PlaceOut, status_code=status.HTTP_201_CREATED)
def create_place(payload: models.PlaceCreate, db: Session = Depends(get_db)):
    place = models.Place(name=payload.name, address=payload.address, rating=payload.rating)
    db.add(place)
    db.commit()
    db.refresh(place)
    return place

@router.get('/places/{place_id}', response_model=models.PlaceOut)
def get_place(place_id: int, db: Session = Depends(get_db)):
    place = db.query(models.Place).filter(models.Place.id == place_id).first()
    if not place:
        raise HTTPException(status_code=404, detail='Place not found')
    return place

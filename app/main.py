from fastapi import FastAPI
from .db import engine, Base
from .routes import router as places_router

app = FastAPI(title='QuietPlaces API')

Base.metadata.create_all(bind=engine)

app.include_router(places_router, prefix='')

from fastapi import FastAPI
from .db import engine, Base
from .routes import router as places_router
from fastapi.staticfiles import StaticFiles

app = FastAPI(title='QuietPlaces API')

Base.metadata.create_all(bind=engine)

app.include_router(places_router, prefix='')

app.mount("/", StaticFiles(directory="app/static", html=True), name="static")

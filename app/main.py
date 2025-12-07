from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .db import engine, Base
from .routes import router as places_router
from fastapi.staticfiles import StaticFiles

app = FastAPI(title='QuietPlaces API')

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)

app.include_router(places_router, prefix='')

app.mount("/", StaticFiles(directory="app/static", html=True), name="static")

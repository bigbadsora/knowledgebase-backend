from fastapi import FastAPI
from app.core.database import Base, engine
from app.api.v1 import note, tag
from dotenv import load_dotenv
import os
from fastapi.middleware.cors import CORSMiddleware

load_dotenv()

# Initialize DB (ensures tables exist)
Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include Routes
app.include_router(note.router, prefix="/api/v1/notes", tags=["Notes"])
app.include_router(tag.router, prefix="/api/v1/tags", tags=["Tags"])

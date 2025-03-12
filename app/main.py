from fastapi import FastAPI
from app.core.database import Base, engine
from app.api.v1 import note, tag

# Initialize DB (ensures tables exist)
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Include Routes
app.include_router(note.router, prefix="/api/v1/notes", tags=["Notes"])
app.include_router(tag.router, prefix="/api/v1/tags", tags=["Tags"])

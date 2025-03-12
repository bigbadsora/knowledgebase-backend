from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional

class NoteBase(BaseModel):
    title: str
    content: str

class NoteCreate(NoteBase):
    pass

class NoteResponse(NoteBase):
    id: int
    created_at: datetime
    updated_at: datetime
    tags: List[str] = []

    class Config:
        orm_mode = True

class NoteUpdate(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None

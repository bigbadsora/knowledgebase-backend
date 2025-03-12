from typing import Optional
from pydantic import BaseModel

class TagBase(BaseModel):
    name: str

class TagCreate(TagBase):
    pass

class TagUpdate(BaseModel):
    name: Optional[str] = None

class TagResponse(TagBase):
    id: int

    class Config:
        orm_mode = True
        
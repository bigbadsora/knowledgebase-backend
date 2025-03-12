from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.core.database import Base
from app.models.note import notes_tags

class Tag(Base):
    __tablename__ = 'tags'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    notes = relationship("Note", secondary=notes_tags, back_populates="tags")

from sqlalchemy import Column, Integer, String, Text, DateTime, Table, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from app.core.database import Base

# Association table for many-to-many relationship between Notes and Tags
notes_tags = Table(
    'notes_tags', Base.metadata,
    Column('note_id', Integer, ForeignKey('notes.id'), primary_key=True),
    Column('tag_id', Integer, ForeignKey('tags.id'), primary_key=True)
)

class Note(Base):
    __tablename__ = 'notes'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    content = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    tags = relationship("Tag", secondary=notes_tags, back_populates="notes")

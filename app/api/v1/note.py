from typing import List
from fastapi import APIRouter, Depends, HTTPException, Response
from sqlalchemy.orm import Session
from app.models.note import Note
from app.schemas.note import NoteCreate, NoteUpdate, NoteResponse
from app.core.database import get_db

router = APIRouter()

@router.get("/", response_model=List[NoteResponse])
def get_notes(db: Session = Depends(get_db)):
    return db.query(Note).all()

@router.get("/{note_id}", response_model=NoteResponse)
def get_note(note_id: int, db: Session = Depends(get_db)):
    note = db.query(Note).filter(Note.id == note_id).first()
    if note is None:
        raise HTTPException(status_code=404, detail="Note not found")
    return note

@router.post("/", response_model=NoteResponse, status_code=201)
def create_note(note: NoteCreate, db: Session = Depends(get_db)):
    db_note = Note(**note.dict())
    db.add(db_note)
    db.commit()
    db.refresh(db_note)
    return db_note

@router.put("/{note_id}", response_model=NoteResponse)
def update_note(note_id: int, note: NoteUpdate, db: Session = Depends(get_db)):
    db_note = db.query(Note).filter(Note.id == note_id).first()
    if db_note is None:
        raise HTTPException(status_code=404, detail="Note not found")
    for key, value in note.model_dump().items():
        if value is not None:
            setattr(db_note, key, value)
    db.commit()
    db.refresh(db_note)
    return db_note

@router.delete("/{note_id}", status_code=204)
def delete_note(note_id: int, db: Session = Depends(get_db)):
    db_note = db.query(Note).filter(Note.id == note_id).first()
    if db_note is None:
        raise HTTPException(status_code=404, detail="Note not found")
    db.delete(db_note)
    db.commit()
    return Response(status_code=204)

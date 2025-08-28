from typing import List, Optional
from fastapi import FastAPI, Depends, Query
from sqlalchemy.orm import Session
from database import SessionLocal
from models import Character
from schemas import CharacterResponse

app = FastAPI()

# Dependency to get a database session
def get_db():
    db = SessionLocal()
    try: 
        yield db
    finally:
        db.close()

ALLOWED_SORT_COLUMNS = {"id", "name", "height"}

# GET /api/v1/characters with optional nation_id query param
@app.get("/api/v1/characters", response_model=List[CharacterResponse])
def read_characters(
    nation_id: Optional[int] = None,
    skip: int = 0,
    limit: int = 20,
    sort_by: Optional[str] = Query("id", regex="^(id|name|height)$"), 
    db: Session = Depends(get_db)
):

    query = db.query(Character)
    
    if nation_id is not None:
        query = query.filter(Character.nation_id == nation_id)

    if sort_by in ALLOWED_SORT_COLUMNS:
        query = query.order_by(getattr(Character, sort_by))
    else:
        query = query.order_by(Character.id)
    
    return query.offset(skip).limit(limit).all()

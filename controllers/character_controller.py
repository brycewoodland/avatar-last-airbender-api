from fastapi import Depends
from sqlalchemy.orm import Session
from typing import List, Optional
from schemas.character import CharacterResponse
from services.character_service import get_characters
from database import get_db

def read_characters_controller(
    db: Session = Depends(get_db),
    nation_id: Optional[int] = None,
    skip: int = 0,
    limit: int = 20,
    sort_by: str = "id"
) -> List[CharacterResponse]:
    return get_characters(db, nation_id, skip, limit, sort_by)

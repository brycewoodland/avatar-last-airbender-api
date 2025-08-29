from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from controllers.character_controller import read_characters_controller
from database import get_db

router = APIRouter(prefix="/api/v1/characters", tags=["characters"])

@router.get("/")
def get_characters(
    db: Session = Depends(get_db),
    nation_id: int | None = None,
    skip: int = 0,
    limit: int = 20,
    sort_by: str = "id"
):
    return read_characters_controller(db, nation_id, skip, limit, sort_by)

from sqlalchemy.orm import Session
from typing import List, Optional
from models.character import Character

ALLOWED_SORT_COLUMNS = {"id", "name", "height"}

def get_characters(
    db: Session,
    nation_id: Optional[int] = None,
    skip: int = 0,
    limit: int = 20,
    sort_by: str = "id"
) -> List[Character]:

    query = db.query(Character)

    if nation_id is not None:
        query = query.filter(Character.nation_id == nation_id)

    if sort_by in ALLOWED_SORT_COLUMNS:
        query = query.order_by(getattr(Character, sort_by))
    else:
        query = query.order_by(Character.id)

    return query.offset(skip).limit(limit).all()

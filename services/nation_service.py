from sqlalchemy.orm import Session
from models.nation import Nation

def get_nations(db: Session):
    return db.query(Nation).all()
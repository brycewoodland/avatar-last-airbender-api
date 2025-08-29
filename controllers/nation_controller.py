from sqlalchemy.orm import Session
from services import nation_service

def get_nations_controller(db: Session):
    return nation_service.get_nations(db)
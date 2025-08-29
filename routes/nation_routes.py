from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from schemas.nation import NationResponse
from controllers import nation_controller
from typing import List

router = APIRouter(prefix="/api/v1/nations", tags=["nations"])

@router.get("/", response_model=List[NationResponse])
def read_nations(db: Session = Depends(get_db)):
    return nation_controller.get_nations_controller(db)
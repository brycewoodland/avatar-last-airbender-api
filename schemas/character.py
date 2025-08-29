from pydantic import BaseModel
from typing import Optional

class CharacterBase(BaseModel):
    name: str
    nation_id: Optional[int] = None
    date_of_birth: Optional[str] = None
    date_of_death: Optional[str] = None
    gender: Optional[str] = None
    height: Optional[float] = None
    hair_color: Optional[str] = None
    eye_color: Optional[str] = None

class CharacterResponse(CharacterBase):
    id: int

    class Config:
        orm_mode = True
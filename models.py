from sqlalchemy import Column, Integer, String, Float, ForeignKey
from database import Base

class Character(Base):
    __tablename__ = "characters"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    nation_id = Column(Integer, ForeignKey("nations.id"))
    date_of_birth = Column(String(30))
    date_of_death = Column(String(30))
    gender = Column(String(20))
    height = Column(Float)
    hair_color = Column(String(50))
    eye_color = Column(String(50))
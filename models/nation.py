from sqlalchemy import Column, Integer, String, Text 
from database import Base

class Nation(Base):
    __tablename__ = "nations"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False, unique=True, index=True)
    description = Column(Text, nullable=True)
from pydantic import BaseModel

class NationBase(BaseModel):
    name: str
    description: str | None = None

class NationResponse(NationBase):
    id: int

    class Config:
        orm_mode = True
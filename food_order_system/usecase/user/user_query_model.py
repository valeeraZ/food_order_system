from pydantic import BaseModel


class UserReadModel(BaseModel):
    name: str
    phone_number: str
    is_verified: bool

    class Config:
        orm_mode = True

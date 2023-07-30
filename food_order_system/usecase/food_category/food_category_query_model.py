from pydantic import BaseModel


class FoodCategoryReadModel(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True

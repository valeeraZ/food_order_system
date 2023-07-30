from pydantic import BaseModel


class FoodItemReadModel(BaseModel):
    id: int
    name: str
    price: float
    image_url: str
    description: str
    category_id: int

    class Config:
        orm_mode = True

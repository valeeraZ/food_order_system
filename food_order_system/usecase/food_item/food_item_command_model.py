from pydantic import BaseModel


class FoodItemCreateModel(BaseModel):
    name: str
    price: float
    category_id: int
    description: str
    image_url: str


class FoodItemUpdateModel(FoodItemCreateModel):
    pass

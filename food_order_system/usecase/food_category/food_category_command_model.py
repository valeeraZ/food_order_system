from pydantic import BaseModel


class FoodCategoryCreateModel(BaseModel):
    name: str

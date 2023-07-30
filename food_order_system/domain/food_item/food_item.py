from dataclasses import dataclass


@dataclass
class FoodItem:
    name: str
    price: float
    image_url: str
    description: str
    is_available: bool

    class Config:
        orm_mode = True

    def __eq__(self, obj: object) -> bool:
        return self.name == obj.name if isinstance(obj, FoodItem) else False

from dataclasses import dataclass


@dataclass
class FoodCategory:
    name: str

    class Config:
        orm_mode = True

    def __eq__(self, obj: object) -> bool:
        return self.name == obj.name if isinstance(obj, FoodCategory) else False

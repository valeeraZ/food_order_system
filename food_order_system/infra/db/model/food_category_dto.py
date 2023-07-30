from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from food_order_system.infra.db.model.base import Base


class FoodCategoryDTO(Base):
    __tablename__ = "food_category"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    food_items = relationship(
        "FoodItemDTO",
        back_populates="category",
        lazy="selectin",
    )

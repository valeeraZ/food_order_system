from sqlalchemy import DECIMAL, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from food_order_system.infra.db.model.base import Base


class FoodItemDTO(Base):
    __tablename__ = "food_item"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    price: Mapped[DECIMAL] = mapped_column(DECIMAL, nullable=False)
    image_url: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str] = mapped_column(String(255), nullable=False)
    category_id: Mapped[int] = mapped_column(Integer, ForeignKey("food_category.id"))
    category = relationship("FoodCategoryDTO", back_populates="food_items")

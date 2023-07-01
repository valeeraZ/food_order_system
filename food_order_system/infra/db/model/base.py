from sqlalchemy.orm import DeclarativeBase

from food_order_system.infra.db.meta import meta


class Base(DeclarativeBase):
    """Base for all models."""

    metadata = meta

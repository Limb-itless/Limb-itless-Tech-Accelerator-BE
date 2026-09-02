from pydantic import BaseModel, ConfigDict


class ItemBase(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


class ItemCreate(ItemBase):
    """Fields accepted when creating an item."""


class ItemRead(ItemBase):
    """Fields returned to API clients."""

    model_config = ConfigDict(from_attributes=True)

    id: int

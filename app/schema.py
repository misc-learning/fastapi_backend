from random import randint
from typing import Literal

from pydantic import BaseModel, Field


class Order(BaseModel):
    """Make order.

    Args:
        BaseModel (_type_): _description_

    """

    price: int
    title: str
    destination: str


class BaseShipment(BaseModel):
    """Initiate data validation class.

    Args:
        BaseModel (_type_): _description_

    """

    article: str = Field(max_length=25)
    weight: float = Field(le=30, ge=0.1)

    destination: int | None = Field(default=randint(1000, 9999))


class ShipmentRead(BaseShipment):
    """Read Shipment.

    Args:
        BaseShipment (_type_): _description_

    """

    status: Literal["in transit", "out for delivery", "placed", "delivered"]


class ShipmentCreate(BaseShipment):
    """Create Shipment.

    Args:
        BaseShipment (_type_): _description_

    """

    order: Order


class ShipmentUpdate(BaseShipment):
    """Update Shipment.

    Args:
        BaseShipment (_type_): _description_

    """

    status: Literal["in transit", "out for delivery", "placed", "delivered"]

from random import randint
from typing import Literal

from pydantic import BaseModel, Field


class Shipment(BaseModel):
    """Initiate data validation class.

    Args:
        BaseModel (_type_): _description_

    """

    article: str = Field(max_length=25)
    weight: float = Field(le=30, ge=0.1)
    status: Literal["in transit", "out for delivery", "placed"]
    destination: int | None = Field(default=randint(1000, 9999))

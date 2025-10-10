from pydantic import BaseModel
from typing import Optional

class ProductCreate(BaseModel):
    id: int
    name: str
    price: float
    discounted_price: Optional[float] = None
    internal_retailer_details: str

class ProductPublic(BaseModel):
    id: int
    name: str
    price: float

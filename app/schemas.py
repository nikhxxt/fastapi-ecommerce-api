# schemas.py
from pydantic import BaseModel
from typing import Optional

class ProductCreate(BaseModel):
    id: int
    name: str
    price: float
    discounted_price: Optional[float]
    internal_retailer_details: str

class ProductResponse(BaseModel):
    id: int
    name: str
    price: float

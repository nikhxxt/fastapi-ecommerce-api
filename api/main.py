from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

# Input model
class ProductCreate(BaseModel):
    id: int
    name: str
    price: float
    discounted_price: Optional[float] = None
    internal_retailer_details: str

# Output model
class ProductPublic(BaseModel):
    id: int
    name: str
    price: float

# In-memory store
products_db = []

@app.post("/products/", response_model=ProductPublic)
def create_product(product: ProductCreate):
    products_db.append(product)
    return ProductPublic(id=product.id, name=product.name, price=product.price)

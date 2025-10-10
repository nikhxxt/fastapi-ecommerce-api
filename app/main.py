from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

# =========================
# Input model (full product data)
# =========================
class ProductCreate(BaseModel):
    id: int
    name: str
    price: float
    discounted_price: Optional[float] = None
    internal_retailer_details: str

# =========================
# Output model (public-facing)
# =========================
class ProductPublic(BaseModel):
    id: int
    name: str
    price: float

# =========================
# In-memory store
# =========================
products_db = []

# =========================
# POST /products/ endpoint
# =========================
@app.post("/products/", response_model=ProductPublic)
def create_product(product: ProductCreate):
    products_db.append(product)
    return ProductPublic(id=product.id, name=product.name, price=product.price)

# =========================
# Optional: Root route to avoid 404
# =========================
@app.get("/")
def welcome():
    return {"message": "Welcome to the E-commerce Product API!"}


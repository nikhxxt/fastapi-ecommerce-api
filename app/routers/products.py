# routes/products.py
from fastapi import APIRouter
from app.schemas import ProductCreate, ProductResponse

router = APIRouter()

@router.post("/products/", response_model=ProductResponse)
def create_product(product: ProductCreate):
    # Normally you'd save to DB here
    return ProductResponse(
        id=product.id,
        name=product.name,
        price=product.price
    )

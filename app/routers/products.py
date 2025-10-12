from fastapi import APIRouter
from app.models import ProductCreate, ProductPublic

router = APIRouter()
product_db = {}

@router.post("/products/", response_model=ProductPublic)
def create_product(product: ProductCreate):
    product_db[product.id] = product
    return ProductPublic(
        id=product.id,
        name=product.name,
        price=product.price
    )

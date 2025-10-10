from fastapi import APIRouter
from app.models import ProductCreate, ProductPublic

router = APIRouter()
product_db = {}

@router.post("/products/", response_model=ProductPublic)
def create_product(product: ProductCreate):
    product_db[product.id] = product
    return ProductPublic(id=product.id, name=product.name, price=product.price)

@router.get("/products/", response_model=dict)
def get_all_products():
    return {
        pid: {
            "id": prod.id,
            "name": prod.name,
            "price": prod.price
        }
        for pid, prod in product_db.items()
    }

@router.get("/admin/products/", response_model=dict)
def get_all_products_admin():
    return {
        pid: prod.dict()
        for pid, prod in product_db.items()
    }

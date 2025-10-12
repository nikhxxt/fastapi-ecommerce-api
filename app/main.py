from fastapi import FastAPI
from app.routers import products

app = FastAPI()

@app.get("/")
def welcome():
    return {"message": "Welcome to the E-commerce Product API!"}

app.include_router(products.router)



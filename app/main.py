# main.py
from fastapi import FastAPI
from app.routes import products

app = FastAPI()
app.include_router(products.router)

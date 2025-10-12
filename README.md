
# 🛒 FastAPI E-commerce Product API

A secure, cloud-deployed FastAPI backend for product creation—designed to mimic platforms like Amazon. This API filters sensitive retailer metadata from customer-facing responses and is deployed on Render.

## 🚀 Live Demo

Access the interactive Swagger UI:
👉 [https://fastapi-ecommerce-api-tagg.onrender.com/docs](https://fastapi-ecommerce-api-tagg.onrender.com/docs)

## 📦 Features

- **POST /products/**: Create a product with full metadata
- **GET /products/**: Retrieve public product data (id, name, price)
- **GET /admin/products/**: Retrieve full internal product data (admin view)
- **Secure Response Filtering**: Sensitive fields like `discounted_price` and `internal_retailer_details` are hidden from public responses

## 🧪 Sample I/O

### Request

```json
POST /products/
Content-Type: application/json

{
  "id": 1,
  "name": "iPhone 15",
  "price": 999.99,
  "discounted_price": 899.99,
  "internal_retailer_details": "Apple_US_2025_Internal"
}
```

### Public Response

```json
{
  "id": 1,
  "name": "iPhone 15",
  "price": 999.99
}
```

## 🧰 Tech Stack

- **FastAPI** for backend
- **Pydantic** for data validation
- **Render** for cloud deployment
- **Swagger UI** for interactive API docs

## 📁 Project Structure

```
app/
├── routers/
│   └── products.py
├── models.py
├── main.py
render.yaml
requirements.txt
```

## ⚙️ Deployment (Render)

```yaml
# render.yaml
services:
  - type: web
    name: fastapi-ecommerce
    env: python
    plan: free
    buildCommand: pip install -r requirements.txt
    startCommand: uvicorn app.main:app --host 0.0.0.0 --port 10000
```

## 📜 License

This project is open-source. You may reuse and adapt it with proper attribution.

---


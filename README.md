# ⚡ FastAPI E-Commerce API

A modular **FastAPI REST API** demonstrating request validation, schema separation, and controlled API responses.

## 🚀 Features

* Product creation with FastAPI
* Request validation using **Pydantic**
* Separate internal and public schemas
* Response filtering with FastAPI `response_model`
* Modular router-based architecture
* Interactive Swagger/OpenAPI documentation
* Deployed on Render

## 🛠️ Tech Stack

**Python 3.10+ · FastAPI · Pydantic · Uvicorn · REST API · Swagger/OpenAPI · Render**

## 🧩 Architecture

```text
fastapi-ecommerce-api/
├── app/
│   ├── routers/
│   │   └── products.py
│   ├── models.py
│   ├── schemas.py
│   └── main.py
├── render.yaml
├── requirements.txt
├── README.md
└── LICENSE
```

The API separates internal product data from customer-facing responses. Fields such as `discounted_price` and `internal_retailer_details` can be accepted in the request but are excluded from the public response using `response_model`.

### Example

**Request**

```json
{
  "id": 1,
  "name": "iPhone 15",
  "price": 999.99,
  "discounted_price": 899.99,
  "internal_retailer_details": "Apple_US_2025_Internal"
}
```

**Public Response**

```json
{
  "id": 1,
  "name": "iPhone 15",
  "price": 999.99
}
```

This demonstrates how the backend can accept internal metadata while exposing only customer-facing fields through the API response schema.

## 🌐 Live API

**API:**
https://fastapi-ecommerce-api-tagg.onrender.com/

**Swagger:**
https://fastapi-ecommerce-api-tagg.onrender.com/docs

The API can be tested directly through Swagger UI.

## 🚀 Run Locally

```bash
git clone https://github.com/nikhxxt/fastapi-ecommerce-api.git
cd fastapi-ecommerce-api
pip install -r requirements.txt
uvicorn app.main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

Swagger documentation:

```text
http://127.0.0.1:8000/docs
```

## 📄 License

MIT License



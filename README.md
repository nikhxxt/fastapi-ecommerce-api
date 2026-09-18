# ⚡ FastAPI E-Commerce API

A modular FastAPI backend demonstrating product creation, data validation, and response filtering. The API accepts product metadata while ensuring that only customer-facing fields are included in responses.

## 🚀 Features

- Product creation using FastAPI
- Pydantic-based request validation
- Response filtering using FastAPI `response_model`
- Separates internal product metadata from public-facing data
- Modular router and schema structure
- Interactive Swagger API documentation
- Deployed on Render
- MIT licensed

## 🛠️ Tech Stack

- Python 3.10+
- FastAPI
- Pydantic
- Uvicorn
- Render
- Swagger UI
- JSON

## 🧩 Project Overview

This project demonstrates how a FastAPI backend can handle product data while controlling which fields are exposed to API consumers.

A product request can contain both public and internal fields. The API uses Pydantic schemas and FastAPI's `response_model` to return only the fields intended for customers.

For example, internal fields such as `discounted_price` and `internal_retailer_details` can be accepted in the request but excluded from the public response.

## 🚀 Quick Start

### 1. Clone the repository

```bash
git clone https://github.com/nikhxxt/fastapi-ecommerce-api.git
cd fastapi-ecommerce-api
````

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the application

```bash
uvicorn app.main:app --reload
```

The API will be available locally through the FastAPI server.

## 📁 Folder Structure

```text
fastapi-ecommerce-api/
├── app/
│   ├── routers/
│   │   └── products.py        # Product API routes
│   ├── models.py              # Internal product models
│   ├── schemas.py             # Request and response schemas
│   └── main.py                # FastAPI application entry point
├── render.yaml                # Render deployment configuration
├── requirements.txt           # Python dependencies
├── README.md                  # Project documentation
└── LICENSE                    # MIT License
```

## 🧪 Sample API Request

### `POST /products/`

Create a product using the API.

**Request:**

```json
{
  "id": 1,
  "name": "iPhone 15",
  "price": 999.99,
  "discounted_price": 899.99,
  "internal_retailer_details": "Apple_US_2025_Internal"
}
```

## 📤 Public Response

The API uses a public response schema to expose only customer-facing fields.

**Response:**

```json
{
  "id": 1,
  "name": "iPhone 15",
  "price": 999.99
}
```

> 🔐 `discounted_price` and `internal_retailer_details` are accepted in the request but excluded from the response using FastAPI's `response_model`.

## 🌐 Swagger API Documentation

Test the API interactively using Swagger UI:

**Live API:**
[https://fastapi-ecommerce-api-tagg.onrender.com/](https://fastapi-ecommerce-api-tagg.onrender.com/)

**Swagger Docs:**
[https://fastapi-ecommerce-api-tagg.onrender.com/docs](https://fastapi-ecommerce-api-tagg.onrender.com/docs)

Swagger provides an interactive interface for sending requests and viewing API responses.

## 🧪 Curl Testing

Example request:

```bash
curl -X POST https://fastapi-ecommerce-api-tagg.onrender.com/products/ \
  -H "Content-Type: application/json" \
  -d '{
    "id": 1,
    "name": "iPhone 15",
    "price": 999.99,
    "discounted_price": 899.99,
    "internal_retailer_details": "Apple_US_2025_Internal"
  }'
```

## ☁️ Deployment

The API is deployed on Render using the `render.yaml` configuration file.

The deployed API can be accessed through:

[https://fastapi-ecommerce-api-tagg.onrender.com/](https://fastapi-ecommerce-api-tagg.onrender.com/)


## 📜 License

This project is licensed under the MIT License. See the [`LICENSE`](https://github.com/nikhxxt/fastapi-ecommerce-api/blob/main/LICENSE) file for details.


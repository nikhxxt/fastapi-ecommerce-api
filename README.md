
# ⚡️ FASTAPI-ECOMMERCE-API  
🛒 Secure Product Creation API

Build a secure, cloud-deployed FastAPI backend for product creation with filtered customer-facing responses.

---

## 🎯 Goal

Implement a modular, token-ready API that:
- Accepts full product metadata
- Returns only public fields to customers
- Is deployed on Render
- Includes Swagger UI for testing

---

## 🔖 Badges

![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)
![Python](https://img.shields.io/badge/Python-3.10-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100.0-brightgreen.svg)
![Render](https://img.shields.io/badge/Deployed%20on-Render-blue.svg)

---

## 📚 Table of Contents

- [Quick Start](#-quick-start)
- [Folder Structure & What’s Included](#-folder-structure--whats-included)
- [Sample I/O](#-sample-io)
- [Swagger & Curl Testing](#-swagger--curl-testing)
- [License & Contact](#-license--contact)

---

## 🚀 Quick Start

```bash
git clone https://github.com/nikhxxt/fastapi-ecommerce-api.git
cd fastapi-ecommerce-api
pip install -r requirements.txt
uvicorn app.main:app --reload
```
---

## 📁 Folder Structure

```
fastapi-ecommerce-api/
├── app/
│   ├── routers/
│   │   └── products.py        # Modular route definitions
│   ├── models.py              # Pydantic models for input/output filtering
│   └── main.py                # FastAPI entry point
├── render.yaml                # Render deployment config
├── requirements.txt           # Python dependencies
├── README.md                  # Project documentation
├── LICENSE                    # MIT License
```

---

## 🧪 Sample I/O

### 🔹 Request

```json
POST /products/
{
  "id": 1,
  "name": "iPhone 15",
  "price": 999.99,
  "discounted_price": 899.99,
  "internal_retailer_details": "Apple_US_2025_Internal"
}
```

### 🔹 Public Response

```json
{
  "id": 1,
  "name": "iPhone 15",
  "price": 999.99
}
```

---

## 🧰 Swagger & Curl Testing

### 🔸 Swagger UI  
Access the interactive API explorer:  
👉 [https://fastapi-ecommerce-api-tagg.onrender.com/docs](https://fastapi-ecommerce-api-tagg.onrender.com/docs)

### 🔸 Curl Command

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


---

## 📜 License & Contact

This project is licensed under the MIT License — see [`LICENSE`](LICENSE).  
📂 Repo: [https://github.com/nikhxxt/fastapi-ecommerce-api](https://github.com/nikhxxt/fastapi-ecommerce-api)
```

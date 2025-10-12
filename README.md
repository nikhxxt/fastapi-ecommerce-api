
# ⚡️ FASTAPI-ECOMMERCE-API  
🛒 **Secure Product Creation API**

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
![Render Deployment](https://img.shields.io/badge/Deployed%20on-Render-blue.svg)

---

## 📚 Table of Contents

- [What’s Included](#-whats-included)
- [Quick Start](#-quick-start)
- [Folder Structure](#-folder-structure)
- [Sample I/O](#-sample-io)
- [Testing](#-testing)
- [Checklist Before Submission](#-checklist-before-submission)
- [License & Contact](#-license--contact)

---

## 📦 What’s Included

- `main.py` — FastAPI entry point  
- `models.py` — Pydantic models for input/output filtering  
- `routers/products.py` — Modular route definitions  
- `render.yaml` — Render deployment config  
- `requirements.txt` — Python dependencies  
- `README.md` — This file  
- `LICENSE` — MIT License

---

## 🚀 Quick Start

```bash
git clone https://github.com/nikhxxt/fastapi-ecommerce-api.git
cd fastapi-ecommerce-api
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Visit Swagger UI:  
👉 [https://fastapi-ecommerce-api-tagg.onrender.com/docs](https://fastapi-ecommerce-api-tagg.onrender.com/docs)

---

## 📁 Folder Structure

```
fastapi-ecommerce-api/ ├── app/ │ ├── routers/ │ │ └── products.py # Modular route definitions │ ├── models.py # Pydantic models for input/output filtering │ └── main.py # FastAPI entry point ├── render.yaml # Render deployment config ├── requirements.txt # Python dependencies ├── README.md # Project documentation ├── LICENSE # MIT License
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

## 🧰 Testing

### 🔸 Swagger UI  
Use the interactive API explorer:  
[https://fastapi-ecommerce-api-tagg.onrender.com/docs](https://fastapi-ecommerce-api-tagg.onrender.com/docs)

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

This project is licensed under the MIT License — see `LICENSE`.  
📂 Repo: [https://github.com/nikhxxt/fastapi-ecommerce-api](https://github.com/nikhxxt/fastapi-ecommerce-api)
```

---

You can copy this directly into your `README.md`. Want me to help you add a badge section with shields.io, or a `CREDITS.md` for open-source polish? Let’s make this repo shine.

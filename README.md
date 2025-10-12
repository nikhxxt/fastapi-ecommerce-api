**# ⚡️ FASTAPI-ECCOMMERCE-API  
🛒 Secure Product Creation API  
Task‑Build a secure, cloud-deployed FastAPI backend for product creation with filtered customer-facing responses.

Goal: Implement a modular, token-ready API that accepts full product metadata but only exposes public fields to customers. Deployed on Render with Swagger UI for testing.

---

🔖 Badges  
License: MIT  
Repo size  
GitHub stars  
GitHub forks  

---

📚 Table of Contents  
- What’s Included  
- Quick Start — Reproduce the API  
- Folder Structure  
- Sample I/O  
- Swagger & Curl Testing  
- Checklist Before Submission  
- License & Contact  

---

📦 What’s Included  
- `main.py` — FastAPI entry point  
- `models.py` — Pydantic models for input/output filtering  
- `routers/products.py` — Modular route definitions  
- `render.yaml` — Render deployment config  
- `requirements.txt` — Python dependencies  
- `README.md` — This file  
- `LICENSE` — MIT License  

---

## 🚀 Quick Start — Reproduce the API

```bash
git clone https://github.com/nikhxxt/fastapi-ecommerce-api.git
cd fastapi-ecommerce-api
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Visit Swagger UI at:  
👉 [https://fastapi-ecommerce-api-tagg.onrender.com/docs](https://fastapi-ecommerce-api-tagg.onrender.com/docs)

---

## 📁 Folder Structure

```
app/
├── routers/
│   └── products.py
├── models.py
├── main.py
render.yaml
requirements.txt
```

---

## 🧪 Sample I/O

### Request

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

### Public Response

```json
{
  "id": 1,
  "name": "iPhone 15",
  "price": 999.99
}
```

---

## 🧰 Swagger & Curl Testing

### Swagger UI  
Visit: [https://fastapi-ecommerce-api-tagg.onrender.com/docs](https://fastapi-ecommerce-api-tagg.onrender.com/docs)

### Curl Command

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
Repo: [https://github.com/nikhxxt/fastapi-ecommerce-api](https://github.com/nikhxxt/fastapi-ecommerce-api)

```


# ⚡️ FASTAPI-ECOMMERCE-API  
🛒 Secure Product Creation API

Build a secure, cloud-deployed FastAPI backend for product creation with filtered customer-facing responses.

---


## 📚 Table of Contents

- [Tech Stack](#-tech-stack)
- [Project Overview](#-project-overview)
- [Badges](#-badges)
- [Features](#-features)
- [Quick Start](#-quick-start)
- [Folder Structure](#-folder-structure)
- [Sample I/O](#-sample-io)
- [Swagger & Curl Testing](#-swagger--curl-testing)
- [Deployment](#-deployment)
- [License & Contact](#-license--contact)
  
---


## 🛠️ Tech Stack

This project is built using modern, production-grade technologies:

- **FastAPI** – High-performance Python web framework for building APIs
- **Pydantic** – Data validation and serialization using Python type hints
- **Uvicorn** – Lightning-fast ASGI server for running FastAPI apps
- **Render** – Cloud platform for deploying web services with CI/CD
- **Python 3.10** – Language runtime with type hinting and async support
- **Swagger UI** – Auto-generated API documentation and testing interface
- **JSON** – Standard format for request/response payloads



---

 ## 🧩 Project Overview

This project implements a secure, modular FastAPI backend for an e-commerce platform. It allows retailers to create product listings with internal metadata while ensuring that only public-facing information is exposed to customers. The API is designed with best practices in mind: modular routing, Pydantic-based data validation, and response filtering using FastAPI’s `response_model`. It is fully containerized and deployed on [Render](https://fastapi-ecommerce-api-tagg.onrender.com).

---

## 🔖 Badges

![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)
![Python](https://img.shields.io/badge/Python-3.10-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100.0-brightgreen.svg)
![Render](https://img.shields.io/badge/Deployed%20on-Render-blue.svg)

---

## 🎯 Features

- ✅ Accepts full product metadata including sensitive internal fields
- ✅ Returns only public fields (`id`, `name`, `price`) to customers
- ✅ Modular FastAPI structure with routers and schemas
- ✅ Swagger UI for interactive API testing
- ✅ Deployed on Render for public access
- ✅ MIT Licensed and ready for portfolio/demo use

---


## 🚀 Quick Start

```bash
# Clone the repository
git clone https://github.com/nikhxxt/fastapi-ecommerce-api.git
cd fastapi-ecommerce-api

# Install dependencies
pip install -r requirements.txt

# Run the app locally
uvicorn app.main:app --reload
```

---

## 📁 Folder Structure

```
fastapi-ecommerce-api/
├── app/
│   ├── routers/
│   │   └── products.py        # Modular route definitions
│   ├── models.py              # Internal Pydantic models
│   ├── schemas.py             # Input/output schemas for request/response
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

> 🔐 Note: `discounted_price` and `internal_retailer_details` are accepted in the request but excluded from the response using `response_model=ProductPublic`.

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

## ☁️ Deployment

This project is deployed on [Render](https://render.com) using the `render.yaml` configuration file.

To deploy your own version:

1. Push your code to a public GitHub repository
2. Create a new Web Service on Render
3. Connect your GitHub repo and select `render.yaml` as the deploy configuration
4. Done! Your API will be live and accessible via HTTPS

Live Demo:  
🌐 [https://fastapi-ecommerce-api-tagg.onrender.com](https://fastapi-ecommerce-api-tagg.onrender.com)

---

## 📜 License & Contact

This project is licensed under the MIT License — see [`LICENSE`](LICENSE).  
📂 Repo: [https://github.com/nikhxxt/fastapi-ecommerce-api](https://github.com/nikhxxt/fastapi-ecommerce-api)

For questions or feedback, feel free to open an issue or fork the repo.

---

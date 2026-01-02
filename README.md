# User Management API  
**FastAPI · JWT · SQLAlchemy · Pytest**

Production-ready REST API for user management, built to demonstrate backend best practices such as secure authentication, clean architecture, and automated testing.

---

## 🚀 Features
- Full CRUD for users
- JWT Authentication (OAuth2 Password Flow)
- Secure password hashing (bcrypt)
- Protected routes with role-safe access
- SQLite by default (PostgreSQL-ready)
- OpenAPI documentation (Swagger & ReDoc)
- Automated tests with Pytest

---

## 🧱 Architecture
The project follows a layered backend architecture:

- **API Layer**: Request/response handling (FastAPI routers)
- **Schemas**: Data validation and serialization (Pydantic)
- **Business Logic**: CRUD operations and rules
- **Data Layer**: SQLAlchemy ORM models
- **Security**: JWT generation and verification

This structure allows scalability, testability, and maintainability.

---

## 🛠 Tech Stack
- FastAPI & Uvicorn
- SQLAlchemy 2.0
- Pydantic
- JWT (python-jose)
- Passlib + bcrypt
- Pytest

---

## ⚙️ Setup

### 1) Create virtual environment
```bash
python -m venv .venv
```
#### Windows
```bash
.venv\Scripts\activate
```
#### macOS / Linux
```bash
source .venv/bin/activate
```
### 2) Install dependencies
```bash
pip install -r requirements.txt
```

### 3) Environment variables
Create a .env file in the root directory:
```env
DATABASE_URL=sqlite:///./app.db
JWT_SECRET=change_this_in_production
```

### ▶️ Run the API
```bash
uvicorn app.main:app --reload
```
Swagger UI:http://127.0.0.1:8000/docs

### 🔐 Authentication Flow (JWT)

1. Create a user  
2. Login  
3. Receive token  


Example header:
Authorization: Bearer<ACCESS_TOKEN>


### 📌 Main Endpoints
| Method | Endpoint              | Description      |
|--------|-----------------------|------------------|
| POST   | `/api/v1/users`       | Create user      |
| POST   | `/api/v1/auth/login`  | Login & get JWT  |
| GET    | `/api/v1/users/me`    | Get current user |
| GET    | `/api/v1/users`       | List users       |
| PUT    | `/api/v1/users/{id}`  | Update own user  |
| DELETE | `/api/v1/users/{id}`  | Delete own user  |

### 🧪 Tests

Run automated tests:
```bash
pytest -q
```

### 🐘 PostgreSQL Support

To use PostgreSQL:

```env
DATABASE_URL=postgresql+psycopg2://USER:PASSWORD@HOST:5432/DBNAME
```

Install driver:
```
pip install psycopg2-binary
```

### 🎯 Purpose

This project was built as a portfolio backend project to demonstrate:

- REST API design
- Authentication & authorization
- Secure data handling
- Clean architecture
- Testing practices

### 📄 License

MIT
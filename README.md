# User Management API (FastAPI + JWT + SQLAlchemy)

REST API for user management with:
- Full CRUD
- JWT authentication (OAuth2 password flow)
- SQLite by default (PostgreSQL supported via `DATABASE_URL`)
- Pytest integration tests

## Tech Stack
- FastAPI, Uvicorn
- SQLAlchemy 2.0
- Pydantic
- JWT (python-jose)
- Password hashing (passlib + bcrypt)

## Setup

### 1) Create virtual environment and install dependencies
```bash
python -m venv .venv
```
# Windows:
```bash
.venv\Scripts\activate
```
# macOS/Linux:
```bash
source .venv/bin/activate

pip install -r requirements.txt
uvicorn app.main:app --reload
```




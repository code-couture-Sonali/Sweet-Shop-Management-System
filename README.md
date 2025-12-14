# Sweet Shop Management System

## Project Description
This project is a full-stack Sweet Shop Management System developed using
FastAPI for backend and React for frontend.

The system allows users to register, login, view sweets, purchase sweets,
and enables admin users to manage inventory.

## Technologies Used
- Backend: FastAPI (Python)
- Frontend: React JS
- Database: SQLite
- Authentication: JWT
- Testing: Pytest
- Version Control: Git

## Features
- User registration and login
- JWT-based authentication
- Add, view, and purchase sweets
- Inventory management
- Protected APIs
- Test-driven development (TDD)

## How to Run Backend
```bash
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload

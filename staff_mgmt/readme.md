# 📋 Staff Management System API

A simple REST API built with Django and Django REST Framework for managing staff, departments, and attendance.

---

## 🔐 Authentication

This API uses **Token Authentication**. You must authenticate before accessing any endpoint.

### 🔑 Get Token
**POST** `/api-auth/`

#### Request Headers:
```http
Content-Type: application/json
```

#### Request Body: (superuser credentials)
```json
{
  "username": "acgabriel", 
  "password": "asdfghjkl"
}
```

#### Sample Response:
```json
{
  "token": "0123456789abcdef"
}
```

Use this token for all requests as a header:

```http
Authorization: Token 0123456789abcdef
```

---

## 📁 API Endpoints

### ✅ All requests must include:

```http
Authorization: Token your_token_here
Content-Type: application/json
```

---

## 🧩 Department Endpoints

### 🔍 GET `/api/departments/`
**Description:** Retrieve all departments  
**Response:**
```json
[
  {
    "id": 1,
    "name": "HR",
    "description": "Handles hiring"
  }
]
```

---

### ➕ POST `/api/departments/`
**Request Body:**
```json
{
  "name": "IT",
  "description": "Tech Department"
}
```

**Response:**
```json
{
  "id": 2,
  "name": "IT",
  "description": "Tech Department"
}
```

---

### 🔍 GET `/api/departments/{id}/`
**Response:**
```json
{
  "id": 1,
  "name": "HR",
  "description": "Handles hiring"
}
```

---

### ✏️ PUT `/api/departments/{id}/`
**Request Body:**
```json
{
  "name": "Human Resources",
  "description": "Updated description"
}
```

---

### ❌ DELETE `/api/departments/{id}/`
**Response:** `204 No Content`

---

## 👨‍💼 Staff Endpoints

### 🔍 GET `/api/staff/`

### ➕ POST `/api/staff/`
```json
{
  "name": "John Doe",
  "email": "john@example.com",
  "department": 1,
  "position": "Manager",
  "hire_date": "2024-01-15"
}
```

---

### 🔍 GET `/api/staff/{id}/`

### ✏️ PUT `/api/staff/{id}/`
```json
{
  "name": "John D.",
  "email": "john@example.com",
  "department": 2,
  "position": "Senior Manager",
  "hire_date": "2024-01-15"
}
```

---

### ❌ DELETE `/api/staff/{id}/`

---

## 📅 Attendance Endpoints

### 🔍 GET `/api/attendance/`

### ➕ POST `/api/attendance/`
```json
{
  "staff": 1,
  "date": "2024-05-05",
  "status": "Present"
}
```

---

### 🔍 GET `/api/attendance/{id}/`

### ✏️ PUT `/api/attendance/{id}/`
```json
{
  "staff": 1,
  "date": "2024-05-05",
  "status": "Absent"
}
```

---

### ❌ DELETE `/api/attendance/{id}/`

---

## 🚨 Error Handling

- **401 Unauthorized**: Missing or invalid token
- **403 Forbidden**: Permission denied
- **400 Bad Request**: Invalid data format
- **404 Not Found**: Resource does not exist

---

## 🚀 Getting Started

### 1. Clone and Install
```bash
git clone https://github.com/yourusername/staff-management-system.git
cd staff-management-system
pip install -r requirements.txt
```

### 2. Run Migrations
```bash
python manage.py migrate
```

### 3. Create Superuser
```bash
python manage.py createsuperuser
```

### 4. Start the Server
```bash
python manage.py runserver
```

---

## 📂 Project Structure

```
staff_mgmt/
│
├── core/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│
├── staff_mgmt/
│   ├── settings.py
│   ├── urls.py
│
├── manage.py
└── README.md
```

---

## 👤 Author

**Ac Gabriel E. Manalo**  
BSIT | Staff Management System - CRUD API using Django

---

## 📝 License

This project is licensed for educational purposes.

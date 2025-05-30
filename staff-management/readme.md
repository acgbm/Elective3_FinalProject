🔐 User Authentication API (Django + JWT)
This API provides basic user authentication using JWT. It allows users to:

Register an account

Log in using their credentials

Access protected routes using tokens

📌 Tech Stack
Django

Django REST Framework (DRF)

SimpleJWT

PostgreSQL

📋 Endpoints & Sample Usage
🔸 Register
Method: POST

URL: /api/register/

Headers:

pgsql
Content-Type: application/json
Request Body:

json
{
  "username": "testuser",
  "password": "testpass123"
}
Sample Response:

json
{
  "message": "User registered successfully",
  "refresh": "<JWT refresh token>",
  "access": "<JWT access token>"
}
🔸 Login
Method: POST

URL: /api/login/

Headers:

pgsql
Content-Type: application/json
Request Body:

json
{
  "username": "testuser",
  "password": "testpass123"
}
Sample Response:

json
{
  "refresh": "<JWT refresh token>",
  "access": "<JWT access token>"
}
🔸 Access Protected Route
Method: GET

URL: /api/protected/

Headers:

pgsql
Authorization: Bearer <your-access-token>
Sample Response:

json
{
  "message": "Hello, testuser!"
}
🔸 Refresh Token
Method: POST

URL: /api/token/refresh/

Headers:

pgsql
Content-Type: application/json
Request Body:

json
{
  "refresh": "<your-refresh-token>"
}
Sample Response:

json
{
  "access": "<new access token>"
}
✅ Security Notes
Passwords are hashed before being stored.

JWT tokens are used for authentication.

Invalid credentials or unauthorized requests return appropriate error messages.

🔧 CRUD API Endpoints (Activity 6)
These endpoints allow authenticated users to Create, Read, Update, and Delete data for three models: Departments, Positions, and Employees.

🔐 Authentication Required
All requests must include a valid JWT access token in the headers:

makefile
Authorization: Bearer <your_access_token>
You can obtain a token by logging in via:

bash
POST /api/token/
📁 Departments
➕ Create Department
Method: POST

URL: /api/departments/

Request Body:

json
{
  "name": "Human Resources"
}
📄 Get All Departments
Method: GET

URL: /api/departments/

🔍 Get Department by ID
Method: GET

URL: /api/departments/<id>/

🔄 Update Department
Method: PUT

URL: /api/departments/<id>/

Request Body:

json
{
  "name": "HR Department"
}
❌ Delete Department
Method: DELETE

URL: /api/departments/<id>/

📁 Positions
➕ Create Position
Method: POST

URL: /api/positions/

Request Body:

json
{
  "title": "Software Engineer"
}
📄 Get All Positions
Method: GET

URL: /api/positions/

🔍 Get Position by ID
Method: GET

URL: /api/positions/<id>/

🔄 Update Position
Method: PUT

URL: /api/positions/<id>/

Request Body:

json
{
  "title": "Senior Software Engineer"
}
❌ Delete Position
Method: DELETE

URL: /api/positions/<id>/

📁 Employees
➕ Create Employee
Method: POST

URL: /api/employees/

Request Body:

json
{
  "name": "John Doe",
  "department": 1,
  "position": 2,
  "email": "john.doe@example.com"
}
📄 Get All Employees
Method: GET

URL: /api/employees/

🔍 Get Employee by ID
Method: GET

URL: /api/employees/<id>/

🔄 Update Employee
Method: PUT

URL: /api/employees/<id>/

Request Body:

json
{
  "name": "John Smith",
  "department": 1,
  "position": 2,
  "email": "john.smith@example.com"
}
❌ Delete Employee
Method: DELETE

URL: /api/employees/<id>/

🔁 Sample Auth Flow (Optional)
Get Token
http
POST /api/token/
Content-Type: application/json

{
  "username": "your_username",
  "password": "your_password"
}
Response:

json
{
  "refresh": "token_string",
  "access": "token_string"
}

## ⏳ Rate Limited Endpoint

### GET /api/limited/

- **Headers:** `Authorization` optional
- **Rate Limit:** 5 requests per 60 seconds per IP
- **Success Response:**
```json
{
  "message": "You are within the request limit."
}
Error Response (429):

json
{
  "detail": "Rate limit exceeded. Try again later."
}

FileUpload

User Registration Endpoint
URL: /api/fileupload/register/

Method: POST

Content-Type: application/json

Payload Example:

json
{
  "username": "john_doe",
  "password": "your_secure_password",
  "email": "john@example.com",
  "photo": null
}
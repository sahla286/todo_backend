TaskManager

 → Tech Stack
   - Frontend: React
   - Backend: Python Django REST Framework (DRF)
   - Database: MySQL
   - Authentication: JWT (Django Simple JWT)

TaskManager Backend (Django DRF)
→ Task Model
   - Title (Required)
   - Description (Optional)
   - Status (Pending, In Progress, Completed)
   - Due Date (Required)

## Error handling

Validate required fields & correct formats
Handle 404 errors (task not found)
JWT authentication for user session management

SQL Injection prevention → Django ORM & parameterized queries
CORS support

## TaskManager - Setup & Deployment Guide

Prerequisites:
Python 
Node js 
React 
MySQL Server
Git

## Backend Setup (Django REST Framework)
1. Clone the Repository
git clone [repository_url]
cd [project_directory]

2.Create & Activate Virtual Environment
python -m virtualenv venv 
venv\scripts\activate

3. Install Dependencies
pip install django djangorestframework django-filter djangorestframework-simplejwt mysqlclient django-cors-headers

4. Configure Database
Update settings.py with your MySQL database credentials:
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '<your_database_name>',
        'USER': '<your_database_user>',
        'PASSWORD': '<your_database_password>',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

5. Run Migrations

python manage.py makemigrations
python manage.py migrate

6. Start the Server
python manage.py runserver


 ## API Endpoints
   - Authentication:
      - `POST /user/` → User registration
      - `POST /tokenpair/` → User login (Token access)
      - `POST /refreshtoken/` → Refresh expired tokens

 → Task Management:
  - `GET /task/tasks/` → List all tasks (with sorting & filtering)
  - `GET /task/tasks/{id}/` → Retrieve a specific task
  - `POST /task/tasks/` → Create a new task
  - `PUT /task/tasks/{id}/` → Update task details
  - `DELETE /task/tasks/{id}/` → Delete a task

 →Calendar:
  - `GET /task/calendar-tasks/` → Get tasks in calendar format

 → JWT Authentication:
- Add `Authorization: Bearer <access_token>` in the request header

Note: Add the access_token in the Authorization header as:

Authorization: Bearer <access_token>


## Authentication:
Use JWT authentication for secure access.Add 'rest_framework_simplejwt' in installed apps, specify authentication_classes
and permission_classes in views.py

##Testing API Endpoints
Test the server using Postman or Thunder Client.

- `POST http://127.0.0.1:8000/user/` → User Registration
- `POST http://127.0.0.1:8000/tokenpair/` → User Login
- `GET http://127.0.0.1:8000/task/tasks/` → List tasks with sorting & filtering
- `GET http://127.0.0.1:8000/task/tasks/{id}/` → Retrieve a specific task
- `PUT http://127.0.0.1:8000/task/tasks/{id}/` → Update task details
- `DELETE http://127.0.0.1:8000/task/tasks/{id}/` → Delete a task
- `GET http://127.0.0.1:8000/task/calendar-tasks/` → List tasks in calendar view


# 🔗 Django REST Framework (DRF) Practice

This repository contains a basic Django REST Framework (DRF) practice project with CRUD operations on the User model.

## 📚 What is Django REST Framework (DRF)?
Django REST Framework (DRF) is a powerful and flexible toolkit for building Web APIs in Django. It provides features like serialization, authentication, permissions, and viewsets to make API development easier and more efficient.

### 🚀 Getting Started with DRF
Follow these basic commands to set up a DRF project:

1. **Install Django and DRF:**
   ```sh
   pip install django djangorestframework
   ```

2. **Create a new Django project:**
   ```sh
   django-admin startproject myproject
   cd myproject
   ```

3. **Create a Django app:**
   ```sh
   python manage.py startapp myapp
   ```

4. **Add `rest_framework` to `INSTALLED_APPS` in `settings.py`**

5. **Apply migrations:**
   ```sh
   python manage.py migrate
   ```

6. **Run the server:**
   ```sh
   python manage.py runserver
   ```

## 🔄 Fundamentals of DRF

### 1. 📚 Models
Models define the database schema using Django's ORM. Each model is a Python class that subclasses `models.Model` and defines fields that map to database columns.

### 2. 🎨 Serializers
Serializers allow complex data types such as Django models to be converted into JSON and vice versa. DRF provides `ModelSerializer` to automatically generate fields based on a model.

### 3. 🕹 Views
Views handle the logic for API requests. DRF provides function-based views (FBVs) and class-based views (CBVs), including generic views for common operations like list, create, retrieve, update, and delete.

### 4. 🛡️ URLs
URLs route API requests to the appropriate views. DRF uses Django's `path()` and `re_path()` functions along with `DefaultRouter` for viewsets.

### 5. ✨ Authentication & Permissions
DRF supports various authentication classes like `TokenAuthentication`, `SessionAuthentication`, and `JWTAuthentication`. Permissions restrict access to API endpoints based on user roles and conditions.

#### 🔑 Simple JWT Authentication
SimpleJWT is a library used for implementing JSON Web Token (JWT) authentication in DRF. It provides `access` and `refresh` tokens for secure authentication.

**Install SimpleJWT:**
```sh
pip install djangorestframework-simplejwt
```

**Configure JWT Authentication in `settings.py`:**
```python
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}
```

### 6. 📀 Pagination
DRF provides built-in pagination classes like `PageNumberPagination` and `LimitOffsetPagination` to manage large querysets efficiently.

### 7. 🌀 Filtering & Ordering
DRF supports filtering and ordering of querysets using `django-filter` and `ordering_fields` to allow dynamic sorting.

## 🚀 Setup & Installation

Follow these steps to set up the project:

1. **Create a virtual environment and activate it:**
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

2. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

3. **Apply migrations:**
   ```sh
   python manage.py migrate
   ```

4. **Run the server:**
   ```sh
   python manage.py runserver
   ```

## 🛠️ API Endpoints

| Method | Endpoint            | Description                  |
|--------|--------------------|------------------------------|
| GET    | `/api/users/`      | Get all users               |
| GET    | `/api/user/`       | Perform CRUD on a single user |
| POST   | `/api/register/`   | Register a new user         |
| POST   | `/api/login/`      | Login user and get tokens   |
| POST   | `/api/token/refresh/` | Refresh the access token  |

## 🏆 License
This project is open-source and available for learning purposes.


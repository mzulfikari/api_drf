# API Project with Django REST Framework

## 📌 Project Overview

This project is a RESTful API built with Django and Django REST Framework, offering features like user authentication, advertisement management, image uploads, and wall posts. It includes JWT authentication and Swagger documentation for API exploration.

---

## ⚙️ Prerequisites

- Python 3.8+ installed  
- Git installed (optional but recommended)  
- Recommended: `virtualenv` for environment isolation (or use built-in venv)

---

## 📥 Installation and Setup Guide

### 1. Clone the Repository

```bash
git clone https://github.com/mzulfikari/api_drf.git
cd api_drf
2. Create and Activate a Virtual Environment
It's highly recommended to use a virtual environment to avoid dependency conflicts.

On Linux/macOS:

bash
Copy
Edit
python3 -m venv venv
source venv/bin/activate
On Windows:

bash
Copy
Edit
python -m venv venv
venv\Scripts\activate
3. Install Dependencies
Make sure pip is up to date:

bash
Copy
Edit
pip install --upgrade pip
Then install all required packages from requirements.txt:

bash
Copy
Edit
pip install -r requirements.txt
4. Configure Environment Variables (Optional)
If your project uses environment variables (e.g., for secret keys or database), create a .env file in the root directory:

env
Copy
Edit
SECRET_KEY=your_secret_key_here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
(If your project currently doesn't support .env, this step can be skipped or added later.)

5. Apply Database Migrations
Run database migrations to prepare the SQLite database:

bash
Copy
Edit
python manage.py migrate
6. Create a Superuser (Optional)
To access Django Admin or create initial users:

bash
Copy
Edit
python manage.py createsuperuser
Follow the prompts.

7. Run the Development Server
Start the server locally:

bash
Copy
Edit
python manage.py runserver
The API will be available at:

cpp
Copy
Edit
http://127.0.0.1:8000/
8. Access API Documentation
Swagger UI is available for interactive API docs and testing:

arduino
Copy
Edit
http://127.0.0.1:8000/swagger/
🔐 Authentication
The API uses JWT authentication.

Obtain token:

Send POST request to /api/token/ with:

json
Copy
Edit
{
  "username": "your_username",
  "password": "your_password"
}
Use token:

Add the token to Authorization header of requests:

makefile
Copy
Edit
Authorization: Bearer your_access_token

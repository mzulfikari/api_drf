API Project with Django REST Framework
📌 Project Overview
"""
This project is a RESTful API built with Django and Django REST Framework, offering features like user authentication, advertisement management, image uploads, and wall posts. It includes JWT authentication and Swagger documentation for API exploration.
"""

⚙️ Prerequisites
"""

Python 3.8+ installed

Git installed (optional but recommended)

Recommended: virtualenv for environment isolation (or use built-in venv)
"""

📥 Installation and Setup Guide
1. Clone the Repository
"""
git clone https://github.com/mzulfikari/api_drf.git
"""

"""
cd api_drf
"""

2. Create a Virtual Environment
On Linux/macOS:

"""
python3 -m venv venv
"""

On Windows:

"""
python -m venv venv
"""

3. Activate the Virtual Environment
On Linux/macOS:

"""
source venv/bin/activate
"""

On Windows:

"""
venv\Scripts\activate
"""

4. Upgrade pip
"""
pip install --upgrade pip
"""

5. Install Dependencies
"""
pip install -r requirements.txt
"""

6. Configure Environment Variables (Optional)
"""
Create a .env file in the root directory with content like:

SECRET_KEY=your_secret_key_here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

If your project doesn't support .env files yet, you can skip this step.
"""

7. Apply Migrations
"""
python manage.py migrate
"""

8. Create a Superuser (Optional)
"""
python manage.py createsuperuser
"""

9. Run the Development Server
"""
python manage.py runserver
"""

Open your browser and visit:

"""
http://127.0.0.1:8000/
"""

10. Access API Documentation (Swagger UI)
"""
http://127.0.0.1:8000/swagger/
"""

🔐 Authentication
Obtain JWT Token
"""
Send POST request to /api/token/ with JSON body:

{
"username": "your_username",
"password": "your_password"
}
"""

Use JWT Token
"""
Include the token in HTTP headers as:

Authorization: Bearer your_access_token
"""


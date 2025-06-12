📌 Project Overview
This project is a RESTful API built with Django and Django REST Framework, offering features like user authentication, advertisement management, image uploads, and wall posts. It includes JWT authentication and Swagger documentation for API exploration.

⚙️ Prerequisites

bash
Copy
Edit
Python 3.8+ installed
bash
Copy
Edit
Git installed (optional but recommended)
bash
Copy
Edit
Recommended: virtualenv for environment isolation (or use built-in venv)
📥 Installation and Setup Guide

Clone the Repository

bash
Copy
Edit
git clone https://github.com/mzulfikari/api_drf.git
bash
Copy
Edit
cd api_drf
Create a Virtual Environment

On Linux/macOS:

bash
Copy
Edit
python3 -m venv venv
On Windows:

bash
Copy
Edit
python -m venv venv
Activate the Virtual Environment

On Linux/macOS:

bash
Copy
Edit
source venv/bin/activate
On Windows:

bash
Copy
Edit
venv\Scripts\activate
Upgrade pip

bash
Copy
Edit
pip install --upgrade pip
Install Dependencies

bash
Copy
Edit
pip install -r requirements.txt
Configure Environment Variables (Optional)
Create a .env file in the root directory with the following content:

env
Copy
Edit
SECRET_KEY=your_secret_key_here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
If your project doesn't support .env files yet, you can skip this step.

Apply Migrations

bash
Copy
Edit
python manage.py migrate
Create a Superuser (Optional)

bash
Copy
Edit
python manage.py createsuperuser
Run the Development Server

bash
Copy
Edit
python manage.py runserver
Open your browser and visit:

plaintext
Copy
Edit
http://127.0.0.1:8000/
Access API Documentation (Swagger UI)

plaintext
Copy
Edit
http://127.0.0.1:8000/swagger/
🔐 Authentication

Obtain JWT Token
Send POST request to /api/token/ with JSON body:

json
Copy
Edit
{
  "username": "your_username",
  "password": "your_password"
}
Use JWT Token
Include the token in HTTP headers as:

plaintext
Copy
Edit
Authorization: Bearer your_access_token


📌 Project Overview
This project is a RESTful API built with Django and Django REST Framework, offering features like user authentication, advertisement management, image uploads, and wall posts. It includes JWT authentication and Swagger documentation for API exploration.

⚙️ Prerequisites
diff
Copy
Edit
- Python 3.8+ installed
cpp
Copy
Edit
- Git installed (optional but recommended)
rust
Copy
Edit
- Recommended: virtualenv for environment isolation (or use built-in venv)
📥 Installation and Setup Guide
1. Clone the Repository
bash
Copy
Edit
git clone https://github.com/mzulfikari/api_drf.git
bash
Copy
Edit
cd api_drf
2. Create a Virtual Environment
On Linux/macOS:

nginx
Copy
Edit
python3 -m venv venv
On Windows:

nginx
Copy
Edit
python -m venv venv
3. Activate the Virtual Environment
On Linux/macOS:

bash
Copy
Edit
source venv/bin/activate
On Windows:

Copy
Edit
venv\Scripts\activate
4. Upgrade pip
css
Copy
Edit
pip install --upgrade pip
5. Install Dependencies
nginx
Copy
Edit
pip install -r requirements.txt
6. Configure Environment Variables (Optional)
Create a .env file in the root directory with the following content:

ini
Copy
Edit
SECRET_KEY=your_secret_key_here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
If your project doesn't support .env files yet, you can skip this step.

7. Apply Migrations
nginx
Copy
Edit
python manage.py migrate
8. Create a Superuser (Optional)
nginx
Copy
Edit
python manage.py createsuperuser
9. Run the Development Server
nginx
Copy
Edit
python manage.py runserver
Open your browser and visit:

cpp
Copy
Edit
http://127.0.0.1:8000/
10. Access API Documentation (Swagger UI)
arduino
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

makefile
Copy
Edit
Authorization: Bearer your_access_token

## 📌 Project Overview

This project is a RESTful API built using Django and Django REST Framework (DRF).  
It provides the following main features:

- User registration, login, and JWT authentication  
- Advertisement management (CRUD)  
- Image upload and handling  
- Wall posts API for user interactions  
- API documentation via Swagger UI  

The API follows REST principles and supports token-based authentication for secure access.

---

## ⚙️ Prerequisites

Make sure you have installed:

```bash
Python 3.8 or higher
```
```
pip (Python package installer)
```
bash
```
Git (optional, for cloning the repository)
```
📥 Installation and Setup
1. Clone the repository
bash
Copy
Edit
git clone https://github.com/mzulfikari/api_drf.git
bash
Copy
Edit
cd api_drf
2. Create and activate a virtual environment
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
3. Upgrade pip
bash
Copy
Edit
pip install --upgrade pip
4. Install dependencies
bash
Copy
Edit
pip install -r requirements.txt
5. (Optional) Configure environment variables
Create a .env file in the root directory (if you want to override default settings):

env
Copy
Edit
SECRET_KEY=your_secret_key_here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
6. Apply database migrations
bash
Copy
Edit
python manage.py migrate
7. Create a superuser (admin)
bash
Copy
Edit
python manage.py createsuperuser
8. Run the development server
bash
Copy
Edit
python manage.py runserver
Visit the API at:

plaintext
Copy
Edit
http://127.0.0.1:8000/
🧰 API Documentation
Swagger UI is available at:

plaintext
Copy
Edit
http://127.0.0.1:8000/swagger/
It provides interactive API documentation and testing.

🔐 Authentication
This project uses JWT (JSON Web Tokens) for authentication.

Obtain token
Send POST request to:

plaintext
Copy
Edit
/api/token/
with JSON body:

json
Copy
Edit
{
  "username": "your_username",
  "password": "your_password"
}
Using the token
Include the received access token in your request headers:

plaintext
Copy
Edit
Authorization: Bearer <access_token>

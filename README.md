API Project with Django REST Framework
📌 Project Overview
This project is a RESTful API built using Django and Django REST Framework (DRF). It provides functionalities for user authentication, advertisement management, image handling, and wall post interactions. The API is designed to be modular, scalable, and easily extendable.

🚀 Features
User Authentication: Implementing JWT-based authentication for secure user access.

Advertisement Management: CRUD operations for advertisements with optional image attachments.

Image Handling: Uploading and retrieving images associated with advertisements.

Wall Posts: Creating, updating, and deleting posts on the wall.

Swagger Documentation: Interactive API documentation for easy testing and exploration.

⚙️ Technologies Used
Django: Web framework for building the API.

Django REST Framework (DRF): Toolkit for building Web APIs.

JWT (JSON Web Tokens): For secure authentication.

SQLite: Database for development and testing.

Swagger: For API documentation and testing.

📥 Installation & Setup
1. Clone the Repository
bash
Copy
Edit
git clone https://github.com/mzulfikari/api_drf.git
cd api_drf
2. Create a Virtual Environment
bash
Copy
Edit
python -m venv venv
3. Activate the Virtual Environment
Windows:

bash
Copy
Edit
  venv\Scripts\activate
Linux/macOS:

bash
Copy
Edit
  source venv/bin/activate
4. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
5. Apply Migrations
bash
Copy
Edit
python manage.py migrate
6. Run the Development Server
bash
Copy
Edit
python manage.py runserver
The API will be accessible at http://127.0.0.1:8000/.

🧪 API Documentation
The API documentation is available through Swagger UI:

arduino
Copy
Edit
http://127.0.0.1:8000/swagger/
Here, you can explore all available endpoints, view request/response formats, and test the API interactively.

🔐 Authentication
The API uses JWT for authentication. To obtain a token:

Send a POST request to /api/token/ with your credentials:

json
Copy
Edit
{
  "username": "your_username",
  "password": "your_password"
}
The response will contain an access token:

json
Copy
Edit
{
  "access": "your_access_token"
}
Include the token in the Authorization header for subsequent requests:

makefile
Copy
Edit
Authorization: Bearer your_access_token

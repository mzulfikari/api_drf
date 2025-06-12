API Project with Django REST Framework
📌 Project Description
This project is a simple API built using Django and Django REST Framework, designed to provide various functionalities such as user account management, advertisements, images, and a Wall feature.
Swagger is also integrated for automatic API documentation.

🚀 Features
User Account Management: Ability to register, login, and manage users.

Advertisements Management: Create, update, and delete advertisements.

Image Management: Upload and manage images.

Wall Management: Post and manage wall posts.

Swagger Documentation: Access API documentation via Swagger UI.

📥 Prerequisites
Python 3.8 or higher

Django 4.2 or higher

Django REST Framework

SQLite (for development environment)

⚙️ Setup Instructions
Clone the repository:

bash
Copy
Edit
git clone https://github.com/mzulfikari/api_drf.git
cd api_drf
Create and activate a virtual environment:

bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Run migrations:

bash
Copy
Edit
python manage.py migrate
Start the development server:

bash
Copy
Edit
python manage.py runserver
🧪 Using the API
After starting the server, you can access the API documentation through Swagger UI:

arduino
Copy
Edit
http://127.0.0.1:8000/swagger/
On this page, you can view all available endpoints and send test requests.

🔐 Authentication
Some endpoints require authentication.
You can obtain an access token via /api/token/ and include it in your request headers as:

makefile
Copy
Edit
Authorization: Bearer <your_token>
📄 Documentation
For full API documentation and usage, visit Swagger UI at:

arduino
Copy
Edit
http://127.0.0.1:8000/swagger/
🛠️ Project Structure
The project includes the following apps:

account: User account management

ads: Advertisement management

images: Image management

Wall_api: Wall posts management


# Lib_management
A Library Management API with Book, Author, and Borrower entities.
A simple Library Management API built with Django REST Framework and JWT Authentication.
It lets you manage authors, books, and borrowers through clean API endpoints.

🚀 Features

✅ Add and list authors
✅ Add and list books with author details
✅ Borrow books (reduces available copies automatically)
✅ JWT Authentication for all protected routes
✅ Clean and easy-to-understand project structure

🛠️ Tech Stack

Python 3.12+

Django 5+

Django REST Framework

SimpleJWT (for JWT authentication)

⚙️ Installation
[1] Clone the Repository
git clone https://github.com/binoopsebastian/Lib_management.git
cd Lib_management

[1] Create and Activate Virtual Environment

Windows:

python -m venv venv
venv\Scripts\activate


macOS/Linux:

python3 -m venv venv
source venv/bin/activate

[3]  Install SimpleJWT

In your virtual environment, run:

pip install djangorestframework-simplejwt

[4] Apply Migrations
python manage.py migrate

[5] Run the Server
python manage.py runserver


Server will start at 👉 http://127.0.0.1:8000/

🔐 JWT Authentication

You can generate and refresh tokens using the following endpoints:

Method	Endpoint	Description
POST	/api/token/	Get access and refresh token
POST	/api/token/refresh/	Refresh access token

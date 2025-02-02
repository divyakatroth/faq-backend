FAQ BACKEND SYSTEM:
This is a Django-based backend system for managing FAQs with support for multi-language translations. The system allows users to create, retrieve, and translate FAQs dynamically using the Google Translate API.

TABLE OF CONTENTS:
1.Features
2.Installation
3.API Usage
4.Contributing

FEATURES:
FAQ Management: Create, retrieve, update, and delete FAQs.

Multi-language Support: Dynamically translate FAQs into multiple languages using the Google Translate API.

REST API: Fully functional REST API for managing FAQs.

Admin Panel: User-friendly admin interface for managing FAQs.

Caching: Optional caching for improved performance.

INSTALLATION:

Prerequisites:
Python 3.9 or higher

Django 4.2 or higher

Django REST Framework

googletrans library

Steps
1.Clone the Repository:
git clone https://github.com/divyakatroth/faq-backend.git
cd faq-backend

2.Create a Virtual Environment:
python -m venv venv

3.Activate the Virtual Environment:
On Windows:
.\venv\Scripts\activate
On macOS/Linux:
source venv/bin/activate

4.Install Dependencies:
pip install -r requirements.txt

5.Run Migrations:
python manage.py migrate

6.Create a Superuser:
python manage.py createsuperuser

7.Start the Development Server:
python manage.py runserver

8.Access the Admin Panel:
Open your browser and go to:
http://127.0.0.1:8000/admin/

API USAGE:
Base URL
http://127.0.0.1:8000/

Endpoints

1.List All FAQs
URL: /faqs/

Method: GET

Query Parameters:
lang: Language code (e.g., en, hi, fr). Default is en.

Example:
GET http://127.0.0.1:8000/faqs/?lang=hi
Response:
[
    {
        "question": "डजांगो क्या है?",
        "answer": "डजांगो पायथन के लिए एक वेब फ्रेमवर्क है।",
        "language": "hi"
    }
]

2.Create a New FAQ
URL: /faqs/

Method: POST

Request Body:
{
    "question": "What is Django?",
    "answer": "Django is a web framework for Python.",
    "language": "en"
}

Example:
POST http://127.0.0.1:8000/faq/
Response:
{
    "question": "What is Django?",
    "answer": "Django is a web framework for Python.",
    "language": "en"
}

CONTRIBUTING:
We welcome contributions! Please follow these steps to contribute:

1.Fork the Repository:
-Fork the repository on GitHub.

2.Clone the Forked Repository:
git clone https://github.com/divyakatroth/faq-backend.git
cd faq-backend

3.Create a New Branch:
git checkout -b feature/your-feature-name

4.Make Changes
Make your changes and test them thoroughly.

5.Commit Your Changes:
git add .
git commit -m "Add your commit message here"

6.Push to Your Branch:
git push origin feature/your-feature-name

7.Create a Pull Request:
Go to the original repository and create a pull request.
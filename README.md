# HRM app for a logistics company

## Description

This human resources management app is designed to make it easier to manage a logistics company employees' and vehicle data effectively. It allows recruitment staff to handle drivers' documents and vehicle documents, add and update them, and get notifications about upcoming expiration of documents, that must be replaced by newer ones.

## Features

- Secure user authentication
- Documents management
- Automated notifications system

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/latk052024latk1/HRM.git
   cd HRM
2. **Create and activate the environment:** ```python -m venv venv
                                             venv\Scripts\activate```
3. **Install dependencies:** `pip install -r requirements.txt`
4. **Set up the database:** `python manage.py migrate`
5. **Create a superuser:** `python manage.py createsuperuser`
6. **Run the development server:** `py manage.py runserver`
7. **Navigate to http://127.0.0.1:8000** to access the application.

## Usage

1. Sign in using the superuser credentials.
2. Add drivers and their documents to the database.
3. Get notified about the documents that will expire soon.

## Technologies used

- Django 4.2
- MySQL 8.x

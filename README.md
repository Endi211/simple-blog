# Simple Blog

A simple blog application built with Django and Python.

## Features
- User authentication (signup, login, logout) <br/>
- Password reset functionality <br/>
- Create, read, update, and delete blog posts <br/>
- User profile management <br/>
- Media file uploads <br/>
- Language switcher

## Installation
### Clone the repository:

` git clone https://github.com/Endi211/simple-blog.git ` <br/>
` cd simple-blog `

### Create and activate a virtual environment:

`python -m venv venv` <br/>
`source venv/bin/activate  #On Windows use venv\Scripts\activate`

### Install the dependencies:

`pip install -r requirements.txt`

### Set up the database:

`python manage.py migrate`

### Create a superuser:

`python manage.py createsuperuser`

### Run the development server:

`python manage.py runserver`

### Access the application:

`Open your browser and navigate to http://127.0.0.1:8000 `


## Configuration
Email Settings <br/>
To enable password reset functionality, configure your email backend settings in settings.py. For example, using Gmail:

```
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'your-email@gmail.com'
EMAIL_HOST_PASSWORD = 'your-app-password'  # Use an App Password if you have 2-step verification enable
```




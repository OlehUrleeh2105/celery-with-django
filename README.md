Welcome to the Django Celery project! Below are the steps to set up and run the project.

## Setting up Virtual Environment

It's recommended to use a virtual environment to manage dependencies for your project.

1. Create a virtual environment (venv):

```bash
python3 -m venv myenv
```

2. Activate the virtual environment:

### On Windows
```bash
myenv\Scripts\activate
```

### On macOS and Linux
```bash
source myenv/bin/activate
```

## Installing Dependencies

Ensure you are inside the activated virtual environment before installing dependencies.

```bash
pip install -r requirements.txt
```

## Setting Environment Variables

1. Copy the `.env.example` file to `.env`.

```bash
cp .env.example .env
```

2. Open the `.env` file and set variables:
   - `EMAIL_HOST_USER`: your email
   - `EMAIL_HOST_PASSWORD`: your App Password (you can create it in Google 2-Step Verification settings)

## Migrations

Before running the project, make sure to apply migrations:

```bash
python manage.py makemigrations
```

```bah
python manage.py migrate
```

This will create necessary database tables based on your Django models.

## Running the Project

Once dependencies, environment variables, and migrations are set up, you can run the project using the following commands:

1. Start Django development server:

```bash
python manage.py runserver
```

2. Start Celery worker:

```bash
celery -A django_celery_project.celery worker --pool=solo -l info
```

3. Start Celery beat for periodic tasks:

```bash
celery -A django_celery_project beat -l INFO
```

## Endpoints

This project has two endpoints:

1. `/sendmail`: Endpoint for sending emails.
2. `/schedulemail`: Endpoint for scheduling emails.

## Celery Configuration

In the project's `django_celery_project/celery.py` file, there's a hardcoded function to schedule periodic tasks:

```python
app.conf.beat_schedule = {
    'send-mail-every-10-min': {
        'task': 'send_mail_app.tasks.send_mail_func',
        'schedule': crontab(minute=10),
    }   
}
```

Adjust the schedule and task as per your project's requirements.

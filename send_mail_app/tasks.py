import datetime
from django.contrib.auth import get_user_model

from celery import shared_task
from django.core.mail import send_mail
from django_celery_project import settings

@shared_task(bind=True)
def send_mail_func(self):
    users = get_user_model().objects.all()
    mail_subject = "Celery Testing"
    for user in users:
        message = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        to_email = user.email
        send_mail(
            subject = mail_subject,
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[to_email],
            fail_silently=True,
        )
    return "Done"

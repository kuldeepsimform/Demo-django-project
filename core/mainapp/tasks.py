from django.contrib.auth import get_user_model
from celery import shared_task
from core import settings


EMAIL_HOST_USER = ''
@shared_task(bind=True)
def task_func(self):
    for i in range(10):
        print(i)
    return "Done"
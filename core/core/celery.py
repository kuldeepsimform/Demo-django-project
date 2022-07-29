from __future__ import absolute_import,unicode_literals
import os

from celery import Celery
from django.conf import settings
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE','core.settings')

app = Celery("core")
app.conf.enable_utc = False

app.conf.update(timezone = 'Asia/Kolkata')

app.config_from_object('django.conf:settings',namespace='CELERY')

# app.conf.beat_schedule = {
#     'send-mail-every-day-at-5':{
#         'task':'mainaap.tasks.send_mail_func',
#         'schedule': crontab(hour=0),
#         # 'args':['mail']
#     }
# }


app.autodiscover_tasks()
@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
    

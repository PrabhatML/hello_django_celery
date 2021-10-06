import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE','django_celery_project.settings')

app = Celery('django_celery_project',broker="amqp://guest:**@localhost:5673//")

app.config_from_object('django.conf:settings',namespace='CELERY')

app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.requests!r}')
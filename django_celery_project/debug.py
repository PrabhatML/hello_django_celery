import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_celery_project.settings')

# Initialize django applicationd
import django
django.setup()


from computation.tasks import add

res = add.delay(2,3)
print(res.status)
print(res.get(timeout=3))
print(res.status)
print(res.failed())
print(res.successful())
print(res.state)
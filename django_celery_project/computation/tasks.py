from celery import shared_task
from django.utils.crypto import get_random_string
from django.contrib.auth.models import User

import string
import time

@shared_task
def add(x,y):
    print("hello")
    time.sleep(10)
    return x+y

@shared_task
def mul(x, y):
    return x * y

@shared_task
def xsum(numbers):
    return sum(numbers)



@shared_task
def create_random_user_accounts(total):
    for i in range(total):
        print("Celery called")
        username = f'user_{get_random_string(10,string.ascii_letters)}'
        email = f'{username}@example.com'
        password = get_random_string(50)
        User.objects.create_user(username=username,email=email,password=password)
    return f"{total} random users created with success!"
    


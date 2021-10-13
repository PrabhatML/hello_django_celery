# Django Celery Demo

## Run Celery 

```
celery -A django_celery_project worker -l INFO --pool=solo
```

### Celery Help
```
celery worker --help
```

## Run Redis
```
sudo service redis-server start
```

### Update conf file
```
sudo nano /etc/redis/redis.conf2555g
```


### Update redis password in conf
```
requirepass pass_here
```


### if redis has password

```
broker_url = 'redis://:Somya@abcd@localhost:6379/0'
result_backend = 'redis://:Somya@abcd@localhost:6379/0'
```

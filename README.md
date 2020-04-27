### 10 Pin Bowling Game  (WIP)
A 10 pin bowling game built using Python/Django with a Rest API support


## Running application with Docker

Clone and add the following to a '.env.dev' file in the root directory:

```
DEBUG=1
SECRET_KEY=foo
DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 [::1]
```

Build the docker image and run the container:

```
docker-compose build
docker-compose up -d
```

then run the following commands:

```
docker-compose exec web python manage.py makemigrations
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser
```

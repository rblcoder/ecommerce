# ecommerce
Django app

python manage.py makemigrations

python manage.py migrate

python manage.py createsuperuser

python manage.py runserver

urls

`http://127.0.0.1:8000/api/products/` product operations.

`http://127.0.0.1:8000/api/orders/` order operations.


docker-compose up --build

https://dev.to/koladev/setup-a-testing-environment-with-docker-and-pytest-django-postresql-schema-issue-2ffo

python manage.py test store

docker-compose -f docker-compose.dev.yml exec -T web python ecommerce_site/manage.py test store

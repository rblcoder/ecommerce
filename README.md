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

Docker commands

docker rm -vf $(docker ps -aq)

To delete all the images,

docker rmi -f $(docker images -aq)

To delete all volumes

docker volume rm $(docker volume ls -q)


docker-compose exec db psql --username=ecommerce_user --dbname=ecommerce

docker inspect ecommerce_pg_data


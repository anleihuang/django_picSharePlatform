install:
	# install from Pipfile
	pipenv install

	# install pacakges individually
	#pipenv install django pillow
	#pipenv install django-imagekit django-annoying
	#pipenv install psycopg2-binary django-storages boto3
	#pipenv install djangorestframework

run-test:
	python manage.py test

run-server:
	python manage.py runserver 0.0.0.0:8000

update-db-model:
	python manage.py makemigrations
	python manage.py migrate

create-superuser:
	python manage.py createsuperuser
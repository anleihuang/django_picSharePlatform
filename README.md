# Picture Sharing Platform

## Introduction
Developed a picture sharing platform through Django MVC pattern which provides the following services
- Authentication & Authorization
- Upload pictures
- Like & Comment
- Follow and Unfollow users

![platform](https://github.com/anleihuang/django_picSharePlatform/blob/master/docs/pic_share_platform.gif width="800" height="600")

Additionally, API is developed for users to create, read, update, and delete a post and create and read a user profile.

![API](https://github.com/anleihuang/django_picSharePlatform/blob/master/docs/API_example.gif width="800" height="600")

## Architecture
- Used Postgresql server to store metadata (such as Post table, User table, Friendship table, Like table and Follow table)
- Used Amazon S3 to store Django's static files (in public S3 bucket)
- Used Amazon S3 to store Django's media files (in private S3 bucket) 
(more [details about connect Django to S3](https://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html))
- Set up S3 endpoint so that the django web service can connect to the private S3 bucket (more [details about Amazon endpoint setup](https://aws.amazon.com/premiumsupport/knowledge-center/s3-private-connection-no-authentication/) )
- Developed APIs through Django REST Framework (DRF) to connect the Postgresql backend
![infra](https://github.com/anleihuang/django_picSharePlatform/blob/master/docs/infra.png width="800" height="600")


## API

|   Endpoint        | HTTP Method   | CRUD Method | Response          |
| ----------------- |:-------------:|:-----------:|------------------:|
| posts/            | GET           | READ        | Get all posts     |
| posts/:id/        | GET           | READ        | Get post details  |
| posts/create      | POST          | CREATE      | Create new post   |
| posts/update/:id  | PUT           | UPDATE      | Update the post   |
| posts/update/:id  | DELETE        | DELETE      | Delete the post   |
| auth/signup       | POST          | CREATE      | Create new user   |
| user/get_profile/:id/  | GET      | READ      | Get user details  |

Examples (through Postman, an API testing tool):

Get all posts:
`GET http://54.153.73.93:8000/:8000/api/v1/post`

Get details of the post which the post pk is 4
`GET http://ip_address:8000/api/v1/post/update/4/`

Delete the post which the post pk is 4
`DELETE http://ip_address:8000/api/v1/post/update/4/`

Create a new user
`http://ip_address:8000/api/v1/auth/signup?username=test&password=testistest&first_name=test&last_name=huang&email=test@gmail.com`

Get info of this user (which the user pk is 7)
`http://ip_address:8000/api/v1/user/get_profile/7`


## Postgresl Results
![psql1](https://github.com/anleihuang/django_picSharePlatform/blob/master/docs/psql_1.png width="400" height="300")
![psql2](https://github.com/anleihuang/django_picSharePlatform/blob/master/docs/psql_2.png width="400" height="300")
![psql3](https://github.com/anleihuang/django_picSharePlatform/blob/master/docs/psql_3.png width="400" height="300")
![psql4](https://github.com/anleihuang/django_picSharePlatform/blob/master/docs/psql_4.png width="400" height="300")

## Installation
```
$ git clone https://github.com/anleihuang/django_picSharePlatform.git
$ cd django_picSharePlatform

# install dependencies
$ make install

# activate the pipenv virtualenv
$ pipenv shell
```

## Implementation
Setup environment variables by adding the following to ~/.bashrc
```
export DJANGO_SECRET_KEY='YOUR_DJANGO_SECRET_KEY' # to generate a secret key https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
export PSQL_USER='YOUR_PSQL_USER'
export PSQL_PW='YOUR_PSQL_PW'
export PSQL_HOST='YOUR_PSQL_PUBLIC_DNS
export AWS_ACCESS_KEY_ID='YOUR_AWS_ACCESS_KEY_ID'
export AWS_SECRET_ACCESS_KEY='YOUR_AWS_SECRET_ACCESS_KEY'
```

Reload the bashrc file
```
$ source ~/.bashrc
```

Make the models into the database schema
```
$ make update-db-model
```

Run the django server
```
$ make run-server
```

Then, launch {EC2 Public DNS}:8000 in the browser


## Testing
Note that when Django conducts testing, it creates a new database ("default"). Therefore, you would need to grant the CREATEDB permission to the user ${YOUR_PSQL_USER}

```
ALTER USER ${YOUR_PSQL_USER} CREATEDB;
```

```
Conduct testing through make command
$ make run-test

# OR through python command
$ python manage.py test
```

## Requirements
- python 3.7
- pipenv # for  python virtual environment
- Django


## Technology stacks
- Django
- Django REST Framework
- Postgresql
- AWS S3

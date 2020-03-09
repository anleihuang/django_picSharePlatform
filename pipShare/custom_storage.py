"""
Custom storage backend

Reference: 
 - https://simpleisbetterthancomplex.com/tutorial/2017/08/01/how-to-setup-amazon-s3-in-a-django-project.html
 - https://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html
"""

from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage


class StaticStorage(S3Boto3Storage):
    bucket_name = "publicstaticfiles"
    location = settings.AWS_STATIC_LOCATION


class PrivateMediaStorage(S3Boto3Storage):
    bucket_name = "privatemediafiles"
    location = "media"
    default_acl = "private"
    file_overwrite = False
    custom_domain = False

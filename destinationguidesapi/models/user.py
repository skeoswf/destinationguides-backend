from django.db import models

class User(models.Model):

    username = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    bio = models.CharField(max_length=400)
    uid = models.CharField(max_length=100)
    is_admin = models.BooleanField(default=True)
    is_author = models.BooleanField(default=True)
    
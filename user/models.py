from django.contrib.auth.models import AbstractUser
from django.db import models
class User(AbstractUser):
    phonenumber = models.CharField(max_length=30, null=True)
    asdads = models.CharField(max_length=23,null=True)
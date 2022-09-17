from django.db import models

class Khoahoc(models.Model):
    tenkhoahoc = models.CharField(max_length=50)
    urlanh=models.CharField(max_length=100)


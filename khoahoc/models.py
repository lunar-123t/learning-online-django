from django.db import models


class Khoahoc(models.Model):
    ten_khoa_hoc = models.CharField(max_length=50)
    url_anh = models.CharField(max_length=100)

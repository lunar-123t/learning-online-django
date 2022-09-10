import uuid

from django.db import models

class Slider(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    image = models.CharField(max_length=1000)
    text = models.CharField(max_length=255)
    order = models.IntegerField(default=0)



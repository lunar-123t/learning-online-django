import uuid

from django.db import models

class Slider(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    image = models.CharField(max_length=1000, default="")
    title = models.CharField(max_length=255, default="")
    subtitle = models.CharField(max_length=255, default="")
    order = models.IntegerField(default=0)



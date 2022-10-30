from datetime import datetime

from django.db import models

from user.models import User


class Chat(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender',null=True)
    is_my_messages = models.BooleanField(default=True)
    message_text = models.CharField(max_length=200,default="")
    message_date = models.DateTimeField(default=datetime.now(), blank=True)
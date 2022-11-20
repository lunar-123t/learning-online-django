from datetime import datetime

from django.db import models

from user.models import User


class AdminAnswer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    message_text = models.CharField(max_length=200, default="")


class Chat(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender', null=True)
    is_my_messages = models.BooleanField(default=True)
    message_text = models.CharField(max_length=200, default="")
    message_date = models.DateTimeField(default=datetime.now(), blank=True)
    id_create = models.ForeignKey(AdminAnswer, on_delete=models.CASCADE, null=True)



import datetime
import os

from django.contrib import admin

from auth import models
from auth.api import serializers
from chat.models import Chat, AdminAnswer


@admin.register(Chat)
class ChatAdmin(admin.ModelAdmin):
    exclude = ('id_create',)
    list_display = ("user",)

    def delete_model(self, request, obj):
        object=obj.id
        super().delete_model(request, obj)
        AdminAnswer.objects.filter(id=object).delete()

@admin.register(AdminAnswer)
class AdminAnswerView(admin.ModelAdmin):
    def save_model(self, request, obj:AdminAnswer, form, change):
        super(AdminAnswerView, self).save_model(request,obj, form, change)
        user=obj.user
        message_text=obj.message_text
        print(obj)
        Chat.objects.create(
                user=user,
                message_text=message_text,
                is_my_messages=False,
                message_date=datetime.datetime.now(),
                id_create=obj
        )
    def delete_model(self, request, obj):
        id=obj.id
        super().delete_model(request, obj)
        Chat.objects.filter(id_create=id).delete()



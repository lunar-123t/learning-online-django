import email

from django.shortcuts import render

# Create your views here.
#
from rest_framework import request

from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

import chat
from chat.api.serializers import MessSerializer
from chat.models import Chat
from user.models import User


class chatApiView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = MessSerializer
    def get_queryset(self):
        login = self.request.user
        print(login)
        return Chat.objects.filter(user=login)
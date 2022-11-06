import email

from django.shortcuts import render

# Create your views here.
#
from rest_framework import request

from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

import chat
from chat.api.serializers import MessSerializer, chatcreateserializers
from chat.models import Chat
from user.models import User


class chatApiView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = MessSerializer
    def get_queryset(self):
        login = self.request.user
        return Chat.objects.filter(user=login)
class chatCreate(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        dataguilen=self.request.data
        serializers = chatcreateserializers(data=dataguilen, context={'request': request})
        if serializers.is_valid():
            chatcreate = serializers.create(serializers.validated_data)
            return Response(chatcreateserializers(chatcreate).data)
        else:
            return Response({"recces":False,"message":"du lieu gui len ko hop le"})
import datetime

from rest_framework import serializers
from rest_framework.serializers import Serializer
from chat.models import Chat


class MessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = ('id', 'is_my_messages', 'message_text')


class ChatCreateserializers(Serializer):
    message_text = serializers.CharField(max_length=200)
    def create(self, validated_data):
        return Chat.objects.create(
            user=self.context.get("request").user,
            message_text=validated_data["message_text"],
            is_my_messages=True,
            message_date=datetime.datetime.now()
        )

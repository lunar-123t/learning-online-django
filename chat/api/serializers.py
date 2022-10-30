from rest_framework import serializers

import chat
from chat.models import Chat


class MessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = ('id','is_my_messages','message_text')
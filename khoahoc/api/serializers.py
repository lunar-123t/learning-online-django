from rest_framework import serializers

from khoahoc.models import Khoahoc



class KhoahocSerializer(serializers.ModelSerializer):
    class Meta:
        model = Khoahoc
        fields = "__all__"
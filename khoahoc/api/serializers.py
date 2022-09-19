from rest_framework import serializers

from khoahoc.models import KhoaHoc, LevelKhoaHoc, MonHoc


class KhoahocSerializer(serializers.ModelSerializer):
    class Meta:
        model = KhoaHoc
        fields = "__all__"


class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = LevelKhoaHoc
        fields = ('ten_level',)


class MonhocSerializer(serializers.ModelSerializer):
    class Meta:
        model = MonHoc
        fields = "__all__"

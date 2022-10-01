from rest_framework import serializers
from rest_framework.response import Response

from khoahoc.models import KhoaHoc, LevelKhoaHoc, MonHoc


class KhoahocSerializer(serializers.ModelSerializer):
    class Meta:
        model = KhoaHoc
        fields = "__all__"


class MonhocSerializer(serializers.ModelSerializer):
    class Meta:
        model = MonHoc
        fields = "__all__"


class LevelSerializer(serializers.ModelSerializer):
    mon_hoc = serializers.SerializerMethodField()

    class Meta:
        model = LevelKhoaHoc
        fields = ('ten_level', 'mon_hoc','id')

    def get_mon_hoc(self, obj:LevelKhoaHoc):
        mon_hoc_list = MonHoc.objects.filter(level=obj)[:4]
        return MonhocSerializer(mon_hoc_list,many=True).data

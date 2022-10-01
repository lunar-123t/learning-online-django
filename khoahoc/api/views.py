from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from khoahoc.api.serializers import KhoahocSerializer, LevelSerializer, MonhocSerializer
from khoahoc.models import KhoaHoc, LevelKhoaHoc, MonHoc


#
class KhoahocApiView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = KhoahocSerializer
    queryset = KhoaHoc.objects.all()

class Listlevel(ListAPIView):
    serializer_class = LevelSerializer
    def get_queryset(self):
        dataguilen = self.request.data
        return LevelKhoaHoc.objects.filter(khoa_hoc_id=dataguilen['idkhoahoc'])


class ListAlllevel(ListAPIView):
    serializer_class = MonhocSerializer

    def get_queryset(self):
        dataguilen = self.request.data
        return MonHoc.objects.filter(level_id=dataguilen['idlevel'])


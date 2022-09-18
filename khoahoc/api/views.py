from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from khoahoc.api.serializers import KhoahocSerializer, LevelSerializer
from khoahoc.models import KhoaHoc, LevelKhoaHoc

#
class KhoahocApiView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = KhoahocSerializer
    queryset = KhoaHoc.objects.all()

# class KhoahocApiView(APIView):
#         permission_classes = [IsAuthenticated]
#
#         def get(self, request, format=None):
#             khoahoc = KhoaHoc.objects.all()
#
#             return Response(data=KhoahocSerializer(khoahoc, many=True).data)


# class LevelApiView(ListAPIView):
#     serializer_class = LevelSerializer
#     queryset = LevelKhoaHoc.objects.all()
#
# # class TestAPI(APIView):
# #     permission_classes = [AllowAny]
# #     def get(self, request):
# #         data = BaiHat.objects.first()
# #         return Response(data=Baihatserializers(data).data)
#
# class  ListAllKhoahoc(ListAPIView)
#     KhoaHoc = KhoaHoc.objects.filter(id=2).first()
#     if KhoaHoc:
#         serializer_class = LevelSerializer
#         queryset = LevelKhoaHoc.objects.all()

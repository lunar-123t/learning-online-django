from rest_framework.generics import ListAPIView

from khoahoc.api.serializers import KhoahocSerializer
from khoahoc.models import Khoahoc


class KhoahocApiView(ListAPIView):
    serializer_class = KhoahocSerializer
    queryset = Khoahoc.objects.all()



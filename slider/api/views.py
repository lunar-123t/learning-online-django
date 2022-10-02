from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny

from slider.api.serializers import SliderSerializer
from slider.models import Slider


class SliderApiView(ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = SliderSerializer
    queryset = Slider.objects.all().order_by('-order')

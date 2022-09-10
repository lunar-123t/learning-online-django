from rest_framework.generics import ListAPIView
from slider.api.serializers import SliderSerializer
from slider.models import Slider


class SliderApiView(ListAPIView):
    serializer_class = SliderSerializer
    queryset = Slider.objects.all()

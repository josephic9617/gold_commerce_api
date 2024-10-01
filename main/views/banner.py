from rest_framework import generics
from main.models.banner import Banner
from main.serializers.banner import BannerSerializer


class BannerView(generics.ListAPIView):
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer
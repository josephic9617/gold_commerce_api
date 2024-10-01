from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from main.models.product import Product
from main.serializers.product import ProductSerializer


class ProductView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductByIDView(APIView):
    def get(self, request, id):
        product = Product.objects.get(id=id)
        serializer = ProductSerializer(product)
        return Response(serializer.data)
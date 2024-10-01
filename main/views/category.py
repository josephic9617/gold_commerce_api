from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from main.models.category import Category
from main.serializers.category import CategorySerializer
from main.models.product import Product
from main.serializers.product import ProductSerializer



class CategoryView(generics.ListAPIView):
    queryset = Category.objects.all().filter(is_root_parent=True)
    serializer_class = CategorySerializer

class ProductByCatIDView(APIView):
    def get(self, request, cat_id):
        products = Product.objects.filter(category__id=cat_id)
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)


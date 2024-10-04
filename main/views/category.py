from rest_framework import generics
from rest_framework.views import APIView
from main.models.category import Category
from main.serializers.category import CategorySerializer
from main.models.product import Product
from main.serializers.product import ProductSerializer
from main.paginations.product import ProductPagination



class CategoryView(generics.ListAPIView):
    queryset = Category.objects.all().filter(is_root_parent=True)
    serializer_class = CategorySerializer

class ProductByCatIDView(generics.ListAPIView):
    serializer_class = ProductSerializer
    pagination_class = ProductPagination

    def get_queryset(self):
        cat_id = self.kwargs.get('cat_id')
        return Product.objects.filter(category__id=cat_id)

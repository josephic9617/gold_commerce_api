from rest_framework import serializers
from main.models.product import Product, ProductImage


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = (
            'category',
            'get_image',
        )

class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True, read_only=True)

    def get_images(self, instance):
        images = instance.productimage_set.all()

    class Meta:
        model = Product
        fields = (
            'id',
            'name',
            'description',
            'price',
            'weight',
            'category',
            'images',
            'created_at',
            'updated_at',
        )
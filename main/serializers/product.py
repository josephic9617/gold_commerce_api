from rest_framework import serializers
from main.models.product import Product, ProductImage, ProductVideo


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = (
            'get_image',
        )

class ProductVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductVideo
        fields = (
            'get_video',
        )

class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True, read_only=True, source='productimage_set')
    videos = ProductVideoSerializer(many=True, read_only=True, source='productvideo_set')

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
            'videos',
            'created_at',
            'updated_at',
        )
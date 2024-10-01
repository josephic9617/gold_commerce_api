from rest_framework import serializers
from main.models.banner import Banner


class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = (
            'id',
            'name',
            'description',
            'get_image',
            'created_at',
            'updated_at',
        )
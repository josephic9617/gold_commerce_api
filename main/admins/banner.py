from django.contrib import admin
from main.models.banner import Banner


class BannerAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'description',
        'get_image',
        'created_at',
        'updated_at',
    )
    list_filter = (
        'name',
        'description',
        'created_at',
        'updated_at',
    )
    search_fields = (
        'id',
        'name',
        'description',
        'get_image',
        'created_at',
        'updated_at',
    )
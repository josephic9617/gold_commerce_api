from django.contrib import admin
from main.models.product import Product, ProductImage

class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'description',
        'price',
        'weight',
        'category',
        'created_at',
        'updated_at',
    )
    list_filter = (
        'name',
        'description',
        'price',
        'weight',
        'category',
        'created_at',
        'updated_at',
    )
    search_fields = (
        'id'
        'name',
        'description',
        'price',
        'weight',
        'created_at',
        'updated_at',
    )

class ProductImageAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'product',
        'get_image',
        'image',
    )
    list_filter = (
        'product',
    )
    search_fields = (
        'id',
        'product',
        'get_image',
        'image',
    )

class ProductVideoAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'product',
        'get_video',
        'video',
    )
    list_filter = (
        'product',
    )
    search_fields = (
        'id',
        'product',
        'get_video',
        'video',
    )
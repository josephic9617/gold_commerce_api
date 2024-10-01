from django.contrib import admin
from main.models.category import Category
from main.admins.category import CategoryAdmin
from main.models.product import Product, ProductImage
from main.admins.product import ProductAdmin, ProductImageAdmin
from main.models.banner import Banner
from main.admins.banner import BannerAdmin



admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductImage, ProductImageAdmin)
admin.site.register(Banner, BannerAdmin)

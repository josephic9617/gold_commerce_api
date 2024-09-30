from django.contrib import admin
from main.models.category import Category
from main.admins.category import CategoryAdmin



admin.site.register(Category, CategoryAdmin)

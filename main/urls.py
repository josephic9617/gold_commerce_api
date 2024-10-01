from django.urls import path
from main.views.category import CategoryView, ProductByCatIDView
from main.views.product import ProductView, ProductByIDView
from main.views.banner import BannerView


urlpatterns = [
    path('categories/', CategoryView.as_view()),
    path('categories/<int:cat_id>/', ProductByCatIDView.as_view()),
    path('products/', ProductView.as_view()),
    path('products/<int:id>/', ProductByIDView.as_view()),
    path('banners/', BannerView.as_view()),
]
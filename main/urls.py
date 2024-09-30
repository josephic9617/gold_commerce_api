from django.urls import path
from main.views.category import CategoryView


urlpatterns = [
    path('categories/', CategoryView.as_view()),
]
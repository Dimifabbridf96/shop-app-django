from django.urls import path
from . import views

urlpatterns = [
    path('clothes/', views.clothes, name='clothes'),
    path('clothes/<int:clothes_id>', views.article_detail, name='article_detail'),
]
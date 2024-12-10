from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('shoes/', views.shoes, name='shoes'),
    path('details/<int:shoe_id>/', views.shoe_detail, name='shoe_detail'),
]
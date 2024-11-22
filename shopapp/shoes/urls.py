from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='shoes_home'),
]
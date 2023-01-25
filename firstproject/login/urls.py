from . import views
from django.urls import path, include
from pathlib import Path


urlpatterns = [
    path('welcome', views.welcome),
]

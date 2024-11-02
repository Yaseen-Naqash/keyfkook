
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home_url'),
    path('under-construction/', views.not_built, name='not_built_url'),
    path('menu/', views.menu, name='menu_url'),


]

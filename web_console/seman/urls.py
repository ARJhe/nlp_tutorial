from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('get/ajax/output', views.semantic_output, name="seman_output"),
]
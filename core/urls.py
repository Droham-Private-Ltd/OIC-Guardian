# core/urls.py
from django.urls import path
from .views import dedup_check

urlpatterns = [
    path('dedup-check', dedup_check),
]
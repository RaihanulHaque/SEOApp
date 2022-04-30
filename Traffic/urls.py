from django.urls import path
from . import views

urlpatterns = [
    path("", views.search, name='search'),
    path("result1/", views.result, name='result1'),
]

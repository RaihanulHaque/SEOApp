from django.urls import path
from . import views

urlpatterns = [
    path("", views.search, name='search'),
    path("result0/", views.result, name='result0'),
]

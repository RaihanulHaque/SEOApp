from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='onpage-home'),
    path('result/', views.result, name='onpage-result'),
]

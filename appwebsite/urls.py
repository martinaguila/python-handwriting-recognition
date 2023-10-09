from django.urls import path
from . import views

urlpatterns = [
    path('', views.hi, name="home-page"),
    path('views.py/', views.my_view, name='my_view'),
]
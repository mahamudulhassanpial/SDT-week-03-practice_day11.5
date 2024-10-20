from django.urls import path, include
from . import views

urlpatterns = [
    path('meal/', views.meal_list, name='meal_list'),
]
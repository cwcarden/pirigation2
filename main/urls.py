
from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home),
    path('controller/', views.controller),
    path('watersettings/', views.water_settings),
    path('config/', views.configurations)
]

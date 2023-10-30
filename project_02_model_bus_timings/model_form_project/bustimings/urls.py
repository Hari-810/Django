from django.urls import path
from . import views

urlpatterns = [
    path('', views.bus_timing_form, name='bus_timing_form'),
    path('bus-search/', views.search_bus, name='search_bus'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('bus-timings/', views.bus_timings, name='bus_timings'),
]

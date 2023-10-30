from django.urls import path
from . import views

urlpatterns = [
    path('', views.form_view, name='form'),
    path('submit/', views.submit_view, name='submit'),
]

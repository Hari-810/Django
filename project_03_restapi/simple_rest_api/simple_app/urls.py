from django.urls import path
from . import views

urlpatterns = [
    path('tasks/', views.get_single_tasks),
    path('multiple_tasks/', views.get_all_tasks),
    path('add_task/',views.create_task),
    ]
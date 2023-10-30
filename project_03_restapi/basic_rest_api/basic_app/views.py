from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Task
from .serializers import TaskSerializer

@api_view(['GET', 'POST'])
def task_list(request):
    if request.method == 'GET':
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def task_detail(request, pk):
    try:
        task = Task.objects.get(pk=pk)
    except Task.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TaskSerializer(task)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


"""

@api_view Decorator:

Purpose:
    The @api_view decorator is specifically designed for creating views that handle HTTP methods for RESTful APIs. 
    It's part of the Django REST framework (DRF), a powerful and flexible toolkit for building Web APIs.

Advantages:

    Simplifies the creation of API views by automatically handling request parsing, response formatting, and common API-related tasks.
    Provides built-in support for handling various HTTP methods (GET, POST, PUT, DELETE, etc.).
    Enforces a more explicit and consistent way of defining API views.
    Integrates seamlessly with DRF's features like authentication, serialization, and permission handling.
    Use Case: Use @api_view when building RESTful APIs with DRF, as it simplifies the development process and provides built-in features tailored for APIs.

"""

# ---------------------------------------------------------------------------------------------------------

"""
    
Traditional Django Views:

Purpose: 
    Traditional Django views are versatile and can be used for various purposes, not limited to APIs. They are part of Django's core framework and are typically associated with rendering HTML pages.

Advantages:

    Offers flexibility to create views that handle both API endpoints and HTML page rendering.
    Allows you to customize the behavior extensively, including response rendering, data processing, and template rendering.
    Use Case: Use traditional Django views when you need to create views for rendering HTML templates, handling non-API-related tasks, or when you require a high degree of customization for your view logic.

"""
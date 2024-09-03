from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from another_app.models import Task
from .serializers import TaskSerializer
# Create your views here.
@api_view(['GET'])
def get_single_tasks(request):
    """
    Returns a JSON response with a single key-value pair, 'name': 'xy12'.

    Example response:
    {
        "name": "xy12"
    }
    """
    data = {'name': "xy12"}
    return Response(data)


@api_view(['GET'])
def get_all_tasks(request):
    
    """
    Returns a JSON response with a list of all tasks in the database.

    Example response:
    [
        {
            "id": 1,
            "title": "Task 1",
            "update_time": "This is task 1."
        },
        {
            "id": 2,
            "title": "Task 2",
            "update_time": "This is task 2."
        }
    ]
    """
    items = Task.objects.all()
    serializer = TaskSerializer(items, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_task(request):
    serilaizer = TaskSerializer(data=request.data)
    if serilaizer.is_valid():
        serilaizer.save()
    return Response()
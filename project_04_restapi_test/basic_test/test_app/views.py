from rest_framework import generics  #generics for creating generic views
from .models import Task
from .serializers import TaskSerializer

class TaskListCreateView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    """
    TaskListCreateView is a class-based view that inherits from generics.ListCreateAPIView. 
        This view is used for handling both the list (GET) and create (POST) operations for tasks.

    queryset = Task.objects.all(): This defines the queryset, which is a collection of all Task objects. 
        It retrieves all tasks from the database.

    serializer_class = TaskSerializer: This specifies the serializer class to be used for serializing and deserializing Task objects. 
        It will use the TaskSerializer defined in serializers.py to convert the task objects into JSON format when sending responses and parse JSON data when receiving requests.
    """
    
    """
    TaskRetrieveUpdateDestroyView is another class-based view that inherits from generics.RetrieveUpdateDestroyAPIView. 
        This view is used for handling the retrieve (GET), update (PUT), and destroy (DELETE) operations for a specific task.

    queryset = Task.objects.all(): Similar to the previous view, it specifies the queryset to include all Task objects.

    serializer_class = TaskSerializer: Again, it specifies the serializer class for working with Task objects.
    
    """
from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

"""
    Serializers play a crucial role in Django REST framework (DRF) when building RESTful APIs. 
    They are used to transform complex data types, such as Django model instances, 
        into Python data types (e.g., dictionaries) that can be easily converted into JSON or XML data. 
"""
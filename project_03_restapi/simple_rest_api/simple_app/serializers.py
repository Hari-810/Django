"""
Import model from another app for serialization
"""


from rest_framework import serializers
from another_app.models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'


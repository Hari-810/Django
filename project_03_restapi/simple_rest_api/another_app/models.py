from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=100)
    update_time = models.DateTimeField( auto_now=True)

"""
Open django db shell

python manage.py shell

from another_app.models import Task
Task.objects.create(title = "ab2") 
Task.objects.create(title = "cd3")

items = Task.objects.all()
print(items)
"""
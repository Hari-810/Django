from django.db import models

# Create your models here.

class BusTiming(models.Model):
    bus_name = models.CharField(max_length=100)
    departure_time = models.TimeField()
    arrival_time = models.TimeField()
    origin = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    
    def __str__(self):
        return self.bus_name

"""
In this model:

BusTiming is a Python class that inherits from models.Model, indicating that it's a Django model.

It has five fields:

    bus_name: A character field (CharField) to store the name of the bus. It has a maximum length of 100 characters.
    departure_time: A time field (TimeField) to store the departure time of the bus.
    arrival_time: A time field (TimeField) to store the arrival time of the bus.
    origin: A character field (CharField) to store the origin of the bus.
    destination: A character field (CharField) to store the destination of the bus.

The __str__ method is defined to return a human-readable representation of the BusTiming instance, which is the bus_name. This is helpful for display purposes in the Django admin panel and other places where the model instance is rendered.

""" 
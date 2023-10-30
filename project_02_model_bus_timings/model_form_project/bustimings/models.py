from django.db import models

class BusTiming(models.Model):
    bus_name = models.CharField(max_length=100)
    departure_time = models.TimeField()
    arrival_time = models.TimeField()
    origin = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)

    def __str__(self):
        return self.bus_name

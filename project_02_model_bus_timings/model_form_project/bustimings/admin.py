from django.contrib import admin
from .models import BusTiming

class BusTimingAdmin(admin.ModelAdmin):
    list_display = ('bus_name', 'departure_time', 'arrival_time', 'origin', 'destination')

admin.site.register(BusTiming, BusTimingAdmin)

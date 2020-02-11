from django.contrib import admin
from .models import Aircraft, Operator, AircraftLoacation

from django.contrib.gis import admin as gis_admin

admin.site.register(AircraftLoacation, gis_admin.GeoModelAdmin)

# Register your models here.
admin.site.register(Aircraft)
admin.site.register(Operator)
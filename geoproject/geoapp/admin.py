from django.contrib import admin
from .models import Aircraft, Operator, AircraftLoacation, User

from django.contrib.gis import admin as gis_admin

admin.site.register(AircraftLoacation, gis_admin.GeoModelAdmin)
from django.contrib.auth.admin import UserAdmin


# Register your models here.
admin.site.register(Aircraft)
admin.site.register(Operator)
admin.site.register(User, UserAdmin)

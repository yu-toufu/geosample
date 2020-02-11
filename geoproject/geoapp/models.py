#from django.db import models
from django.contrib.gis.db import models as models


# Create your models here.
class Operator(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    name = models.CharField(max_length=50)
    created_date = models.DateTimeField()
    updated_date = models.DateTimeField()

    def __str__(self):  
        return self.id 


class Aircraft(models.Model):
    r_id = models.CharField(max_length=50, primary_key=True)
    operator = models.ForeignKey(Operator, on_delete=models.CASCADE)
    created_date = models.DateTimeField()
    updated_date = models.DateTimeField()

    def __str__(self):  
        return self.r_id 


class AircraftLoacation(models.Model):
    aircraft = models.ForeignKey(Aircraft, on_delete=models.CASCADE)
    report = models.DateTimeField()
    geom = models.PointField(srid = 4326)
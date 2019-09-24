from django.db import models

# Create your models here.

class Miles(models.Model):
    vehicle = models.CharField(primary_key=True, max_length=100, unique=True, blank=False)
    total_miles = models.FloatField()

    def __str__(self):
        return f'Name: {self.vehicle} total_miles: {self.total_miles}'
 
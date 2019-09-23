from django.db import models

# Create your models here.

class Miles(models.Model):
    vehicle = models.CharField(max_length=100, unique=True, blank=False)
    total_miles = models.FloatField()
 
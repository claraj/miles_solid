from django.shortcuts import render
from rest_framework import viewsets 
from .models import Miles 
from .serializers import MilesSerializer

# Create your views here.

class MilesViewSet(viewsets.ModelViewSet):
    queryset = Miles.objects.all().order_by('vehicle')
    serializer_class = MilesSerializer

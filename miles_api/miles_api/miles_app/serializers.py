from .models import Miles 
from rest_framework import serializers 

class MilesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Miles
        fields = [ 'vehicle', 'total_miles' ]
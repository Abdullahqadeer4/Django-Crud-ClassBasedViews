from rest_framework import serializers
from crud.models import *

class locationserializer(serializers.ModelSerializer):
    class Meta:
        model=location
        fields='__all__'
        
class itemserializer(serializers.ModelSerializer):
    class Meta:
        model=items
        fields='__all__'
        
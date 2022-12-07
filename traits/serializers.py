from rest_framework import serializers
from .models import Trait

class TraitSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()


    

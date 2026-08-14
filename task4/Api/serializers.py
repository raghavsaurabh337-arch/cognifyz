from rest_framework import serializers
from .models import recode

class recodeSerializer(serializers.ModelSerializer):
    class Meta:
        model=recode
        fields='__all__'
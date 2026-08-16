from rest_framework import serializers
from .models import recode,create

class recodeSerializer(serializers.ModelSerializer):
    class Meta:
        model=recode
        fields='__all__'

class createSerializer(serializers.ModelSerializer):
    class Meta:
        model=create
        fields='__all__'        
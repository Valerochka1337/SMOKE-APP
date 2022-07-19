from rest_framework import serializers
from .models import Liquid


class LiquidSerializer(serializers.ModelSerializer):
    class Meta:
        model = Liquid
        fields = '__all__'

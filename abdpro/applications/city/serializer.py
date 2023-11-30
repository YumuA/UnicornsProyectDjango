from rest_framework import serializers, pagination

from .models import(
    City
)

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ('__all__')
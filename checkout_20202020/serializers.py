from rest_framework import serializers
from .models import *

class CarritoSerial(serializers.ModelSerializer):
    class Meta:
        model = CarritoCompras
        fields = '__all__'


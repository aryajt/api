from rest_framework import serializers
from .models import Devices_test

class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Devices_test
        fields = '__all__'
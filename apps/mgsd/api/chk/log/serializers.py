from .models import Log
from rest_framework import serializers


class XLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Log
        fields = '__all__'
        # depth = 1

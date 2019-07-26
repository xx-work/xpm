from rest_framework import serializers
# from rest_framework.response import Response
# from rest_framework import status

from .models import InfoSecEvent


class InfoSecEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = InfoSecEvent
        fields = '__all__'



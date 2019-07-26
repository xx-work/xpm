from rest_framework import serializers
# from rest_framework.response import Response
# from rest_framework import status

from .models import BackUpHistory


class BackUpHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BackUpHistory
        fields = '__all__'



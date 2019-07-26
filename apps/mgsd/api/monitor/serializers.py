from rest_framework import serializers
# from rest_framework.response import Response
# from rest_framework import status

from .models import ProcessAuditLog, ObjProcess


class ObjProcessSerializer(serializers.ModelSerializer):
    class Meta:
        model = ObjProcess
        fields = '__all__'


class ProcessAuditLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProcessAuditLog
        fields = '__all__'


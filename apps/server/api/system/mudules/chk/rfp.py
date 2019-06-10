from rest_framework import serializers, viewsets, routers
from .models import ChangeAudit


class ChangeAuditSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChangeAudit
        fields = '__all__'


class SystemPolicyCentralizedManagementViewSet(viewsets.ModelViewSet):
    queryset = ChangeAudit.objects.all()
    serializer_class = ChangeAuditSerializer
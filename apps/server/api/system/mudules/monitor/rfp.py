from rest_framework import serializers, viewsets, routers
from .snmp.models import SnmpHostData, SnmpAgentCfgInfo


class SnmpAgentCfgInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = SnmpAgentCfgInfo
        fields = '__all__'


class SnmpHostDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = SnmpHostData
        fields = '__all__'




class SnmpAgentCfgInfoViewSet(viewsets.ModelViewSet):
    queryset = SnmpAgentCfgInfo.objects.all()
    serializer_class = SnmpAgentCfgInfoSerializer


class SnmpHostDataViewSet(viewsets.ModelViewSet):
    queryset = SnmpHostData.objects.all()
    serializer_class = SnmpHostDataSerializer
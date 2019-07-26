from rest_framework import serializers
# from rest_framework.response import Response
# from rest_framework import status


from .models import SnmpAgentCfgInfo, SnmpHostData
from mgsd.xtool.xmodel import XmodelSerializer


class SnmpAgentCfgInfoSerializer(XmodelSerializer):
    class Meta:
        model = SnmpAgentCfgInfo
        fields = '__all__'
        # depth = 1


class SnmpHostDataSerializer(XmodelSerializer):
    class Meta:
        model = SnmpHostData
        fields = '__all__'
        depth = 2

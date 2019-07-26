# coding:utf-8
import json
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes

# from secs.utils.db_utils import from_sql_get_data


@api_view(['GET'])
@permission_classes(())
def collect_data(request):
    from agent.tasks import sysdatas2db
    sysdatas2db.delay()
    return Response({"stat": True, "sync": "同步基本数据库信息已经执行"}, status=201)


from rest_framework import viewsets, routers
from mgsd.xtool.xmodel import XModelViewSet
from .models import SnmpHostData, SnmpAgentCfgInfo
from .serializers import SnmpAgentCfgInfoSerializer, SnmpHostDataSerializer


class SnmpHostDataViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = SnmpHostData.objects.all()
    serializer_class = SnmpHostDataSerializer


class SnmpAgentCfgInfoViewSet(XModelViewSet):
    queryset = SnmpAgentCfgInfo.objects.all()
    serializer_class = SnmpAgentCfgInfoSerializer


snmp_router = routers.DefaultRouter()
snmp_router.register(r'snmpcfg', SnmpAgentCfgInfoViewSet)
snmp_router.register(r'snmpdata', SnmpHostDataViewSet)

snmp_urlparterns = snmp_router.urls 
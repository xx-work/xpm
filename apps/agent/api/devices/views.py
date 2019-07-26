# coding:utf-8

from rest_framework import viewsets, routers
# from mgsd.xtool.xmodel import XModelViewSet
from .models import AgentApi
from .serializers import AgentApiSerializer


class AgentApiSerializerViewSet(viewsets.ModelViewSet):
    queryset = AgentApi.objects.all()
    serializer_class = AgentApiSerializer


agentapi_router = routers.DefaultRouter()
agentapi_router.register('^agent_api', AgentApiSerializerViewSet)
agentapi_urlparterns = agentapi_router.urls
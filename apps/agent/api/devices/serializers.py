from rest_framework import serializers
# from rest_framework.response import Response
# from rest_framework import status
# from mgsd.xtool.xmodel import XmodelSerializer

from .models import AgentApi


class AgentApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgentApi
        fields = '__all__'
        # depth = 1
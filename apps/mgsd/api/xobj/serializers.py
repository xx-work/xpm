from rest_framework import serializers
# from rest_framework.response import Response
# from rest_framework import status
from django.conf import settings
AUTH_USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')

from .models import ConnectManagerUserInfo, SysManagerCopInfo
from mgsd.xtool.xmodel import XmodelSerializer


class CopSerializer(XmodelSerializer):
    class Meta:
        model = SysManagerCopInfo
        fields = '__all__'
        # depth = 1


class ConnectManagerUserInfoSerializer(XmodelSerializer):
    class Meta:
        model = ConnectManagerUserInfo
        fields = '__all__'
        # depth = 2

from mgsd.xtool.xmodel import XModelViewSet

from .models import ConnectManagerUserInfo, SysManagerCopInfo
from .serializers import CopSerializer, ConnectManagerUserInfoSerializer


class CopViewSet(XModelViewSet):
    queryset = SysManagerCopInfo.objects.all()
    serializer_class = CopSerializer


class ConnUserViewSet(XModelViewSet):
    queryset = ConnectManagerUserInfo.objects.all()
    serializer_class = ConnectManagerUserInfoSerializer


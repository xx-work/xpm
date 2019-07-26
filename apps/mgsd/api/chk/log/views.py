from rest_framework import serializers, viewsets, routers

from .models import Log
from .serializers import XLogSerializer


class XlogViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Log.objects.all()
    serializer_class = XLogSerializer
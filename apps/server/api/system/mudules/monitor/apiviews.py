from rest_framework import serializers, viewsets, routers
from .models import HostService


class HostServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = HostService
        fields = '__all__'


class HostServiceViewSet(viewsets.ModelViewSet):
    queryset = HostService.objects.all()
    serializer_class = HostServiceSerializer
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
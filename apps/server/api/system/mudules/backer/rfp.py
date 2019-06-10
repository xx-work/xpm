from rest_framework import serializers, viewsets, routers
from .models import BackUpHistory


class BackUpHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BackUpHistory
        fields = '__all__'


class BackUpHistoryViewSet(viewsets.ModelViewSet):
    queryset = BackUpHistory.objects.all()
    serializer_class = BackUpHistorySerializer
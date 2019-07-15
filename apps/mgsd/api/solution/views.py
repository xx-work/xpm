from rest_framework import serializers, viewsets, routers

from .models import InfoSecEvent
from .serializers import InfoSecEventSerializer


class InfoSecEventViewSet(viewsets.ModelViewSet):
    queryset = InfoSecEvent.objects.all()
    serializer_class = InfoSecEventSerializer


infosec_router = routers.DefaultRouter()
infosec_router.register(r'info_secs', InfoSecEventViewSet)

from django.urls import include, path
urlparterns = [
    path('e2/', include(infosec_router.urls) )
]





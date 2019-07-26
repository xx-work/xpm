from rest_framework import serializers, viewsets, routers

from .xobj.views import ConnUserViewSet, CopViewSet

from .chk.log.views import XlogViewSet

mgsd_router = routers.DefaultRouter()
mgsd_router.register(r'cop', CopViewSet)
mgsd_router.register(r'conn_user', ConnUserViewSet)
mgsd_router.register(r'xlog', XlogViewSet)


from django.urls import include, path
urlparterns = [
    path('xapi/', include(mgsd_router.urls) )
]
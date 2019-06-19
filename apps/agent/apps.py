from __future__ import unicode_literals

from django.apps import AppConfig


class LocalAppConfig(AppConfig):
    name = 'agent'
    verbose_name = "管理平台客户端"
    def ready(self):
        # from . import signals_handler
        return super().ready()
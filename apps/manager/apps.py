from __future__ import unicode_literals

from django.apps import AppConfig


class LocalAppConfig(AppConfig):
    name = 'manager'
    verbose_name = "管理平台服务端"
    orderIndex_ = 10

    def ready(self):
        # from . import signals_handler
        return super().ready()
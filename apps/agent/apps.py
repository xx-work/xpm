from __future__ import unicode_literals

from django.apps import AppConfig


class LocalAppConfig(AppConfig):
    name = 'agent'

    def ready(self):
        # from . import signals_handler
        return super().ready()
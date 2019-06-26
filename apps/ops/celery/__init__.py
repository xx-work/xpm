# -*- coding: utf-8 -*-

import os

from celery import Celery, platforms
platforms.C_FORCE_ROOT = True


# Todo: Set ENV and autodiscover_tasks based in django-beat
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'website.settings')
os.environ.setdefault('FORKED_BY_MULTIPROCESSING', '1')

# from website import settings
from website import settings

# from django.conf import settings

app = Celery('cso')


configs = {k: v for k, v in settings.__dict__.items() if k.startswith('CELERY')}
app.namespace = 'CELERY'
app.conf.update(configs)

# print([app_config.split('.')[0] for app_config in INSTALLED_APPS])
app.autodiscover_tasks(lambda: [app_config.split('.')[0] for app_config in settings.INSTALLED_APPS] )
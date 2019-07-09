# coding:utf-8
from django.conf.urls import url, include


from .views import backup, recover

urlpatterns = [
    url('backup/1rewq3432frewqrewqfdaf/$', backup, name='backup'),
    url('recover/1rewq3432frewqrewqfdaf/$', recover, name='recover'),
]

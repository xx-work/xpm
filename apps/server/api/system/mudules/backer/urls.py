from django.conf.urls import url

#
# from .views import *

from .scripts.plat_backup import recover_plat_db, backup_plat_db

urlpatterns = [
    url(r'^recover_plat_db', recover_plat_db),
    url(r'^backup_plat_db', backup_plat_db),
]

from django.db import models
from django.utils.translation import ugettext_lazy as _
import uuid


class BackUpHistory(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)

    opreate_username = models.CharField(verbose_name="平台操作者", max_length=33)
    backup_path = models.CharField(verbose_name="备份的位置", max_length=33, )
    backup_host = models.CharField(verbose_name="备份的主机", max_length=33, default="Host")
    backup_type = models.CharField(verbose_name="备份类型", max_length=55, default="远程文件备份")

    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table="backup_hostory"
        verbose_name="备份记录"

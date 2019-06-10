from django.db import models
import uuid

from server.api.system.models import SysManagerCopInfo


class HostService(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    belongCop = models.ForeignKey(SysManagerCopInfo, on_delete=models.CASCADE, related_name="cso_cop_service")
    port = models.CharField(max_length=7, verbose_name=u"端口")
    hostname = models.CharField(max_length=55, verbose_name=u"主机名", blank=True)
    banner = models.CharField(max_length=155, verbose_name=u"产品", blank=True)
    protocol = models.CharField(max_length=255, verbose_name=u"协议")
    state = models.CharField(max_length=255, verbose_name=u"状态")
    service = models.CharField(max_length=255, verbose_name=u"服务")
    version = models.CharField(max_length=255, verbose_name=u"版本")
    reason = models.CharField(max_length=255, verbose_name=u"反馈原因", blank=True)
    descover_time = models.DateTimeField(verbose_name="发现时间")
    running = models.BooleanField(verbose_name="服务开启", default=True)

    class Meta:
        db_table="host_service"
        verbose_name="主机服务探测"


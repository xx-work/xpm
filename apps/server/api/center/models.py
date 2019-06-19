from django.db import models
from django.utils.translation import ugettext_lazy as _
import uuid

from ..xobj.models import SysManagerCopInfo
from ..monitor.models import STATES

class SystemPolicyCentralizedManagement(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    cop = models.ForeignKey(SysManagerCopInfo, verbose_name="系统部件", on_delete=models.CASCADE, related_name="cop_center")
    # sys_component = models.CharField(max_length=32, verbose_name="系统部件ID", default="WAF")
    sys_except_handle = models.CharField(max_length=155, verbose_name="异常处理的信息", default="WAF设备CYA-6000存在3条告警信息")
    sys_stat = models.CharField(verbose_name="系统部件状态", max_length=33, choices=STATES, default='RUNING')
    sys_dbackup = models.CharField(max_length=32, verbose_name="系统备份策略描述", default=u"数据最新于2019-4-27 0:0:2备份")
    sys_user = models.CharField(max_length=32, verbose_name="系统连接用户", default="admin001")

    class Meta:
        db_table="policy_cen_mg"
        verbose_name="系统策略集中管理"


class SecurityPolicyCentralizedManagement(SystemPolicyCentralizedManagement):
    add_time = models.DateTimeField(auto_now_add=True, verbose_name="添加时间")

    class Meta:
        db_table="sec_cen_mg"
        verbose_name="安全机制集中管理"

## 这个也许先不用


class AuditPolicyCentralizedManagement(SystemPolicyCentralizedManagement):
    add_time = models.DateTimeField(auto_now_add=True, verbose_name="添加时间")

    class Meta:
        db_table="aduit_cen_mg"
        verbose_name="审计机制集中管理"
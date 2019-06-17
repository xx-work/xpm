from django.db import models
from django.utils.translation import ugettext_lazy as _
import uuid


class SystemPolicyCentralizedManagement(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    uniq_flag = models.CharField(max_length=32, verbose_name="系统部件唯一标识", unique=True) ## 系统资源配置关联
    # sys_component = models.CharField(max_length=32, verbose_name="系统部件ID", default="WAF")
    sys_except_handle = models.CharField(max_length=32, verbose_name="异常处理的信息", default="WAF设备CYA-6000存在3条告警信息")
    sys_stat = models.IntegerField(verbose_name="系统部件状态", default=1)
    sys_dbackup = models.CharField(max_length=32, verbose_name="系统备份策略描述", default=u"数据最新于2019-4-27 0:0:2备份")
    sys_user = models.CharField(max_length=32, verbose_name="系统连接用户", default="admin001")

    class Meta:
        db_table="policy_cen_mg"
        verbose_name="系统策略集中管理"


class SecurityPolicyCentralizedManagement(SystemPolicyCentralizedManagement):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)

## 这个也许先不用



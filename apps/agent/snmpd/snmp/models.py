from django.db import models
from django.utils.translation import ugettext_lazy as _
import uuid

from server.api.models import SysManagerCopInfo


SnmpVersionChoices = (
    (1, 1),
    (2, 2),
    (3, 3),
)


class SnmpAgentCfgInfo(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    cop = models.OneToOneField(SysManagerCopInfo, verbose_name="平台中的系统部件", on_delete=models.CASCADE, related_name="snmp_cfg_of_cop")
    snmp_port = models.IntegerField(verbose_name="Snmp端口", default=161)
    snmp_community = models.CharField(max_length=32, verbose_name="Snmp组织密码")

    # snmp_ver = models.IntegerField(verbose_name="snmp版本", default=2, choices=SnmpVersionChoices)
    # snmp_user = models.CharField(max_length=32, verbose_name="Snmp用户", blank=True)
    # snmp_password = models.CharField(max_length=32, verbose_name="Snmp密码", blank=True)
    # snmp_group = models.CharField(max_length=32, verbose_name="Snmp用户组", blank=True)

    collected = models.BooleanField(verbose_name="是否收集", default=True)

    class Meta:
        db_table="snmp_agent_cfg_info"
        verbose_name="Snmp配置信息"


class SnmpHostData(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    cop = models.ForeignKey(SysManagerCopInfo, verbose_name="平台中的系统部件", on_delete=models.CASCADE, related_name="snmp_data_of_cop")
    send_flow = models.FloatField( verbose_name="发送的字节数", default=0.0)
    recv_flow = models.FloatField( verbose_name="接受字节数", default=0.0)
    cpu_percent = models.FloatField( verbose_name="CPU占用", default=0.0)
    mem_percent = models.FloatField( verbose_name="内存占用", default=0.0)
    disk_percent = models.FloatField( verbose_name="硬盘占用", default=0.0)
    up_time = models.IntegerField(verbose_name="开启时间", blank=True, default=0)

    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table="snmp_agent_data"
        verbose_name="SNMP部件监控数据"

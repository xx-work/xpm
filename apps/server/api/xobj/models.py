from django.db import models
from django.utils.translation import ugettext_lazy as _
import uuid

ProtocalSets = (
    ('ssh', 'SSH'),
    ('http', 'HTTP'),
    ('https', 'HTTPS'),
    ('snmp', 'SNMP'),
    ('smb', 'SMB'),
    ('ftp', 'FTP'),
    ('smtp', 'SMTP')
)


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


# 当前信息都是手动填写
class SysManagerCopInfo(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    uniq_flag = models.CharField(max_length=155, verbose_name="系统部件唯一标识", unique=True)  ## 系统资源配置关联
    name = models.CharField(max_length=128, verbose_name=u"系统部件名称")
    ip = models.GenericIPAddressField(verbose_name=_('ip'))
    type = models.CharField(max_length=128, verbose_name=u"系统部件的类型", default="CommonHost")
    level = models.CharField(max_length=128, verbose_name=u"安全等级", default="High")
    pushed = models.BooleanField(verbose_name="接入", default=True)
    os = models.CharField(max_length=128, verbose_name=u"操作系统", default="Linux")
    mac = models.CharField(max_length=128, verbose_name=u"mac地址",  blank=True)
    mac_vendor = models.CharField(max_length=128, verbose_name=u"厂家",  blank=True)
    up = models.BooleanField(verbose_name="存活状态", default=True)
    extra = models.TextField(verbose_name=u"额外补充信息", default="")
    comment = models.TextField( verbose_name=u"系统部件描述", default="")
    managers = models.ManyToManyField("ConnectManagerUserInfo", related_name="sys_cop_conn_users")
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "sys_cop_info"
        verbose_name = "安全设备系统部件信息"


class ConnectManagerUserInfo(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    name = models.CharField(max_length=128, verbose_name=_('Name'))
    username = models.CharField(max_length=32, blank=True, verbose_name=_('Username'))
    _password = models.CharField(max_length=256, blank=True, null=True, verbose_name=_('Password'))
    _token = models.CharField(max_length=256, blank=True, null=True, verbose_name=_('WebToken'))
    _private_key = models.TextField(max_length=4096, blank=True, null=True, verbose_name=_('SSH private key'))
    _public_key = models.TextField(max_length=4096, blank=True, verbose_name=_('SSH public key'))
    comment = models.TextField(blank=True, max_length=1024, verbose_name=_('Comment'))
    _protocal = models.CharField(max_length=32, default="ssh", verbose_name="管理的协议", choices=ProtocalSets)
    extra_info = models.CharField(max_length=255, blank=True, verbose_name=u"真实的补充信息")
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    # created_by = models.CharField(max_length=128, null=True, verbose_name=_('Created by'))
    # belong_plat = models.CharField(max_length=32, blank=True, verbose_name="归属平台")
    # belong_cop = models.ForeignKey(SysManagerCopInfo, on_delete=models.CASCADE, related_name="sys_cop_conn_user")

    class Meta:
        db_table = "sys_cop_user"
        verbose_name = "系统部件用户"


# class SysManagerCopPolicy(models.Model):
#     id = models.UUIDField(default=uuid.uuid4, primary_key=True)
#     ip = models.CharField(max_length=128, verbose_name=_('ip'))
#     belong_cop = models.ForeignKey(SysManagerCopInfo, on_delete=models.CASCADE, related_name="sys_cop_conn_policy")
#     name = models.CharField(max_length=128, verbose_name=u"系统部件策略描述")
#     comment = models.TextField(max_length=4096, blank=True, verbose_name=u"系统部件描述")
#     _connect_host = models.TextField(blank=True, verbose_name=u"系统部件的server_host")
#     _connect_main = models.CharField(max_length=256, blank=True, verbose_name=u"关联的核心URL和请求方法")
#     _connect_kwargs = models.TextField(blank=True, verbose_name=u"系统部件关联的信息|url参数等")
#     date_created = models.DateTimeField(auto_now_add=True)
#     date_updated = models.DateTimeField(auto_now=True)
#
#     class Meta:
#         db_table = "sys_cop_policy"
#         verbose_name = "系统部件策略"
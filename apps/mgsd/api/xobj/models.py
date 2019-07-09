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

LevelSets = (
    ("High", "高"),
    ("Midium", "中"),
    ("Low", "低"),
)

CopTypes = (
    ("CommonServer", "普通服务器、终端设备操作系统"),
    ("ServerDb", "服务器数据库管理系统"),
    ("Softd", "应用软件系统"),
    ("Openvas", "网络脆弱性扫描系统"),
    ("Netd", "路由器交换机网络设备"),
    ("Firewalld", "防火墙系统"),
    ("IDS/IPS", "入侵检测/防御系统"),
    ("MISP", "统一威胁管理系统"),
    ("Gelid", "网络和终端隔离设备"),
    ("NetdWorkDivice", "联网办公设备"),
    ("NetdPhisicalDivice", "联网的物理安全设施"),
    ("Others", "其他"),
)


# 当前信息都是手动填写
class SysManagerCopInfo(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    uniq_flag = models.CharField(max_length=155, verbose_name="系统部件唯一标识", unique=True)  ## 系统资源配置关联
    name = models.CharField(max_length=128, verbose_name=u"系统部件名称")
    ip = models.GenericIPAddressField(verbose_name=_('ip'))
    type = models.CharField(max_length=128, verbose_name=u"系统部件的类型", choices=CopTypes)
    level = models.CharField(max_length=128, verbose_name=u"安全等级", default="High", choices=LevelSets)
    pushed = models.BooleanField(verbose_name="接入", default=False)
    os = models.CharField(max_length=128, verbose_name=u"操作系统", default="Linux")
    mac = models.CharField(max_length=128, verbose_name=u"mac地址",  blank=True)
    mac_vendor = models.CharField(max_length=128, verbose_name=u"厂家",  blank=True)
    up = models.BooleanField(verbose_name="存活状态", default=True)
    extra = models.TextField(verbose_name=u"额外补充信息", blank=True)
    # comment = models.TextField( verbose_name=u"系统部件描述", default="")
    managers = models.ManyToManyField("ConnectManagerUserInfo",
                                      verbose_name="系统部件管理用户",
                                      related_name="sys_cop_conn_users",
                                      blank=True)

    date_created = models.DateTimeField(auto_now_add=True, verbose_name="部件接入时间")
    date_updated = models.DateTimeField(auto_now=True, verbose_name="部件信息修改时间")

    def __str__(self):
        return str(self.name)

    class Meta:
        db_table = "sys_cop_info"
        verbose_name = "安全设备系统部件信息"


IdentityTypes = (
    ("sysuser", "系统管理员"),
    ("secuser", "安全管理员"),
    ("auduser", "审计管理员"),
    ("superuser", "特权管理员"),
)

STATES = (
    ("RUNING", "正常"),
    ("STOPED", "停止"),
    ("APPENDING", "启动中"),
)


class ConnectManagerUserInfo(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    name = models.CharField(max_length=128, verbose_name=u'用户机制名')
    username = models.CharField(max_length=32, blank=True, verbose_name=_('Username'))
    _password = models.CharField(max_length=256, blank=True, null=True, verbose_name=_('Password'))
    _identity = models.CharField(max_length=66, verbose_name="部件管理身份", default="superuser", choices=IdentityTypes)
    _token = models.CharField(max_length=256, blank=True, null=True, verbose_name=_('WebToken'))
    _private_key = models.TextField(max_length=4096, blank=True, null=True, verbose_name=_('SSH private key'))
    _public_key = models.TextField(max_length=4096, blank=True, verbose_name=_('SSH public key'))
    # comment = models.TextField(blank=True, max_length=1024, verbose_name=_('Comment'))
    _protocol = models.CharField(max_length=32, default="http", verbose_name="管理的协议", choices=ProtocalSets)

    email = models.CharField(max_length=100, default="test@example.com", verbose_name="默认登记邮箱")
    create_user = models.CharField(max_length=100, default="admin001", verbose_name="创建者")
    extra_info = models.CharField(max_length=255, blank=True, verbose_name=u"真实的补充信息")
    is_active = models.BooleanField(verbose_name="生效", default=True)
    date_created = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    date_updated = models.DateTimeField(auto_now=True)
    # created_by = models.CharField(max_length=128, null=True, verbose_name=_('Created by'))
    # belong_plat = models.CharField(max_length=32, blank=True, verbose_name="归属平台")
    # belong_cop = models.ForeignKey(SysManagerCopInfo, on_delete=models.CASCADE, related_name="sys_cop_conn_user")

    def __str__(self):
        # return self.name + "[" + self.username +"]"
        return self.name

    @staticmethod
    def set_password(text):
        from agent.crypto.aes_agent import encrypted
        return encrypted(text)

    def get_password(self):
        from agent.crypto.aes_agent import decriptd
        return decriptd(self._password)

    class Meta:
        db_table = "sys_cop_user"
        verbose_name = "系统部件用户及连接信息"


class AuditLogObject(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    name = models.CharField(max_length=128, verbose_name='审计对象名称')
    cop = models.ForeignKey(SysManagerCopInfo, verbose_name="审计对象部件", related_name='cop_to_audit', on_delete=models.CASCADE)
    table_name = models.CharField(max_length=128, verbose_name='表名', blank=True)
    managers = models.ManyToManyField("ConnectManagerUserInfo", verbose_name="审计管理用户",  related_name="audit_conn_users",blank=True)
    state = models.CharField(max_length=32, default="RUNING", verbose_name="状态", choices=STATES)
    date_created = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    showd = models.BooleanField(verbose_name='展示', default=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "audit_obj"
        verbose_name = "审计对象"

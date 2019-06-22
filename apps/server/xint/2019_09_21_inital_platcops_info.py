# coding:utf-8


from src import django_setup

"""
    uniq_flag = models.CharField(max_length=155, verbose_name="系统部件唯一标识", unique=True)  ## 系统资源配置关联
    name = models.CharField(max_length=128, verbose_name=u"系统部件名称")
    ip = models.GenericIPAddressField(verbose_name=_('ip'))
    type = models.CharField(max_length=128, verbose_name=u"系统部件的类型", choices=CopTypes)
    level = models.CharField(max_length=128, verbose_name=u"安全等级", default="High", choices=LevelSets)
    pushed = models.BooleanField(verbose_name="接入", default=True)
    os = models.CharField(max_length=128, verbose_name=u"操作系统", default="Linux")
    mac = models.CharField(max_length=128, verbose_name=u"mac地址",  blank=True)
    mac_vendor = models.CharField(max_length=128, verbose_name=u"厂家",  blank=True)
    up = models.BooleanField(verbose_name="存活状态", default=True)
    extra = models.TextField(verbose_name=u"额外补充信息", blank=True)
    # comment = models.TextField( verbose_name=u"系统部件描述", default="")
    managers = models.ManyToManyField("ConnectManagerUserInfo","""

CopsInfo = [
{"uniq_flag": "cya_cso_6000_v1", "ip":"192.168.2.55", "type": "MISP", "os": "Centos 7.4",
 "mac": "52:54:00:C0:9C:E7", "level": "High", "mac_vendor": "Nexcom International", "name": "安全管理控制平台"},
{"uniq_flag": "cya_waf_6000_v1", "ip":"192.168.2.73", "type": "Firewalld", "os": "Centos 7.4",
 "mac": "52:54:00:89:DF:1C", "level": "High", "mac_vendor": "QEMU virtual NIC", "name": "WEB应用防火前系统"},
{"uniq_flag": "cya_iruser_6000_v1", "ip": "192.168.2.175", "type": "Openvas", "os": "Centos 7.4",
 "mac": "52:54:00:7F:1B:87","level": "High", "mac_vendor": "Wistron Infocomm (Zhongshan)", "name": "网络脆弱性扫描系统"},
{"uniq_flag": "cya_ips_6000_v1", "ip": "192.168.2.6", "type": "IDS/IPS", "os": "Centos 7.4",
 "mac": "52:54:00:89:DF:3F","level": "High", "mac_vendor": "QEMU virtual NIC", "name": "入侵防御系统"},
]

def inintal_cops(delete=True):
    django_setup()
    import logging
    from server.models import SysManagerCopInfo

    if delete:
        SysManagerCopInfo.objects.all().delete()

    flugs = [x.uniq_flag for x in SysManagerCopInfo.objects.all() ]
    for x in CopsInfo:
        if x["uniq_flag"] not in flugs:
            SysManagerCopInfo.objects.create(**x)
            logging.info("创建对象成功。")
            print("创建对象成功。")


UsersInfo = [
    {"name":"特权用户admin001", "username":"admin001", "_password": "112233..", "_identity":"superuser"},
    {"name":"系统管理员用户admin002", "username":"admin002", "_password": "112233..", "_identity":"sysuser"},
    {"name":"安全管理员用户admin003", "username":"admin003", "_password": "112233..", "_identity":"secuser"},
    {"name":"审计管理员用户admin004", "username":"admin004", "_password": "112233..", "_identity":"auduser"},

]


def inital_users(delete=True):
    django_setup()
    import logging
    from server.models import ConnectManagerUserInfo

    if delete:
        ConnectManagerUserInfo.objects.all().delete()

    Usernames = [x.username for x in ConnectManagerUserInfo.objects.all() ]
    for x in UsersInfo:
        if x["username"] not in Usernames:
            ConnectManagerUserInfo.objects.create(**x)
            logging.info("创建对象成功。")
            print("创建对象成功。")


def inital_progress():
    pass


if __name__ == '__main__':
    inintal_cops()
    inital_users()




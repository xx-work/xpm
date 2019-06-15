from django.db import models
from django.contrib.auth.models import Group, User
from django.utils.translation import ugettext_lazy as _

IdentityChoices = (
    # ('Guest', '游客'),
    # ('WebUser', '平台用户'),
    ('NetworkManager', '安全管理员'),
    ('DbUser', '审计员'),
    ('SuperManager', '管理员'),
)

import uuid

# 2018-9-10 创建 暂未启用
## 用户基本信息
class UserProfile(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)

    desc = models.CharField(u"请求URL", max_length=255, default=u"描述： 无")
    truename = models.CharField(u"真实名字", max_length=55, default=u"未填写")

    _private_key = models.TextField(max_length=4096, blank=True, null=True, verbose_name=_('SSH private key'))
    _public_key = models.TextField(max_length=4096, blank=True, verbose_name=_('SSH public key'))

    # identity = models.CharField(u"身份", max_length=55, default="游客")
    identity = models.CharField(choices=IdentityChoices, default='Guest', max_length=50)
    passwd = models.CharField(u"明文密码", max_length=55, default="1q2w3e4r")
    remarks = models.CharField(u"备注", max_length=55, default="Guest")
    extra = models.CharField(u"备用字段", max_length=155, default=u"无备注描述")

    user = models.ForeignKey(User, related_name='cso_platform_user', on_delete=models.CASCADE)
    # group = models.ForeignKey(Group, verbose_name="用户组", related_name="userprofile_conn_group", on_delete=models.CASCADE)


    class Meta:
        verbose_name = u"用户信息"
        db_table = "userprofile"


StatusChoices = (
    ('200', '正常'),
    ('400', '请求错误'),
    ('403', '访问阻断'),
    ('401', '认证失败'),
    # ('Guest', '游客'),
)


# 访问记录
class UserAuditLog(models.Model):
    url = models.CharField(u"请求URL", max_length=255, default="/waf/mg/jwt_login/")
    request_method = models.CharField(u"请求方法", max_length=255, default="POST")
    args = models.TextField(u"操作参数", default="-")
    ip = models.GenericIPAddressField(u"IP", default="0.0.0.0")
    username = models.CharField(u"访问的用户的用户名", max_length=255)
    status = models.CharField(u"请求状态", choices=StatusChoices, max_length=5, default='200')
    opreate_time = models.DateTimeField(u"操作时间", auto_now=True, editable=False)
    # 这个参数 2019-6-14 版本舍弃
    param = models.CharField(u"参数", max_length=255, default='')

    group = models.ForeignKey(Group, verbose_name="用户组", related_name="community_conn_group", on_delete=models.CASCADE)

    class Meta:
        verbose_name = u"审计用户操作"
        db_table = "user_auditlog"
        ordering = ["-opreate_time"]


# 组织机构
class Community(models.Model):
    group = models.ForeignKey(Group, verbose_name="用户组", related_name="community_conn_group", on_delete=models.CASCADE)
    community_name = models.CharField(u"组织名称", max_length=200)
    responsibility = models.TextField(u"责任书", default="-")

    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name = u"审计用户操作"
        db_table = "community"
        ordering = ["-date_updated"]
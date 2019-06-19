from django.db import models
from django.utils.translation import ugettext_lazy as _
import uuid


CHANGE_STATUS = (
    ('APPENDING', 'APPENDING'), # 变更中
    ('FAILED', 'FAILED'),   # 变更失败
    ('SECCUSS', 'SECCUSS'), # 变更成功
    ('ROLLING', 'ROLLING'), # 变更回滚
)

from django.contrib.auth.models import User


# 之所以不用外键， 是因为当用户名没有的时候，仍然可以提供日志时间的记录。
class ChangeAudit(models.Model):
    """
    注意这个里面的变更记录, 是通过Web中间件进行返回。脚本添加和反馈。
    """
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)

    opreate_username = models.ForeignKey(User, verbose_name="操作者", on_delete=models.CASCADE, related_name="plat_user_chk")
    change_subject = models.CharField(verbose_name="变更的主体", max_length=155, blank=True)
    change_object = models.CharField(verbose_name="变更受体", max_length=155, blank=True)
    # change_type = models.CharField(verbose_name="变更类型", max_length=33, choices=PolicyBaseTypes)

    change_desc = models.CharField(verbose_name="变更描述", max_length=155)
    change_stat = models.CharField(verbose_name="变更状态", max_length=10, choices=CHANGE_STATUS, default="SECCUSS")

    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table="change_audit"
        verbose_name="平台变更记录"


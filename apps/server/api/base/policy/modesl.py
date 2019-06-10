from django.db import models
import uuid

PolicyBaseTypes = (
    ('plat', '平台策略'),
    ('system', '系统管理策略'),
    ('security', '安全机制策略'),
    ('audit', '审计机制策略')
)

from cso.models import SysManagerCopInfo, ConnectManagerUserInfo


class PolicyBase(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    name = models.CharField(max_length=255, verbose_name="策略基准名称")
    desc = models.CharField(max_length=255, verbose_name="策略基准描述")
    type = models.CharField(choices=PolicyBaseTypes, max_length=255, verbose_name="策略基准关联的脚本类型", default="system")
    belong_cop = models.ForeignKey(SysManagerCopInfo, on_delete=models.CASCADE, related_name="sys_cop_conn_policy_base")

    plat_username = models.CharField(max_length=255, verbose_name="关联的平台用户", blank=True)
    cop_user = models.ForeignKey(ConnectManagerUserInfo, on_delete=models.CASCADE, verbose_name="关联的部件用户", blank=True, related_name="sys_copuser_conn_policy_base")

    key = models.CharField(max_length=255, verbose_name="参数名称", blank=True)
    value = models.CharField(max_length=255, verbose_name="参数值", blank=True)
    #kwargs = models.TextField( verbose_name="组合参数群", blank=True)

    class Meta:
        db_table="policy_base"
        verbose_name="策略基准"


class PolicyRule(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    name = models.CharField(max_length=255, verbose_name="策略基准名称")
    desc = models.CharField(max_length=255, verbose_name="策略基准描述")
    type = models.CharField(choices=PolicyBaseTypes, max_length=255, verbose_name="策略基准关联的脚本类型")
    belong_cop = models.ForeignKey(SysManagerCopInfo, on_delete=models.CASCADE, related_name="sys_cop_conn_policy_rule")

    plat_username = models.CharField(max_length=255, verbose_name="关联的平台用户", blank=True)
    cop_user = models.ForeignKey(ConnectManagerUserInfo, on_delete=models.CASCADE, verbose_name="关联的部件用户", blank=True, related_name="sys_copuser_conn_policy_rule")

    key = models.CharField(max_length=255, verbose_name="参数名称", blank=True)
    value = models.CharField(max_length=255, verbose_name="参数值", blank=True)

    active=models.BooleanField(verbose_name="生效", default=True)
    #kwargs = models.TextField(verbose_name="组合参数群", blank=True)

    class Meta:
        db_table = "policy_rule"
        verbose_name = "策略规则"

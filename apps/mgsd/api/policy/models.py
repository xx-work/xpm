from django.db import models
import uuid

PolicyBaseTypes = (
    # ('plat', '平台策略'),
    ('system', '系统管理策略'),
    ('security', '安全机制策略'),
    ('audit', '审计机制策略')
)

from ..xobj.models import SysManagerCopInfo, ConnectManagerUserInfo


class PolicyBench(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    name = models.CharField(max_length=255, verbose_name="策略基准名称")
    desc = models.CharField(max_length=255, verbose_name="策略基准描述")
    type = models.CharField(max_length=50, verbose_name="基准类型", choices=PolicyBaseTypes)
    date_created = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    def __str__(self):
        return str(self.name) + "["+ str(self.type) +"]"

    class Meta:
        db_table="policy_bench"
        verbose_name="策略基准"


RESPONSE_FILTER_TYPES = (
    ("json", "json"),
    ("html", "html"),
    ("txt", "txt"),
)


# 策略的动作 可以使多个用户绑定这个策略执行的动作。
class PolicyAction(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    cop_user = models.ManyToManyField(ConnectManagerUserInfo,
                                      verbose_name="关联的部件用户",
                                      blank=True,
                                      related_name="policy_action_users")
    action_name = models.CharField(max_length=233, verbose_name='策略动作名称', blank=True)
    belong_cop = models.ForeignKey(SysManagerCopInfo, verbose_name="部件应用", on_delete=models.CASCADE, related_name="cop_policy_conn")

    _connect_agent = models.TextField(blank=True, verbose_name=u"系统部件的host")
    _connect_kwargs = models.TextField(blank=True, verbose_name=u"系统部件关联的信息|url参数等")

    date_created = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.action_name

    class Meta:
        db_table = "policy_action"
        verbose_name = "策略动作"
        ordering = ('-date_created',)


class PolicyActionHistory(models.Model):
    policyaction = models.ForeignKey(PolicyAction, on_delete=models.CASCADE, related_name="action_policy_history")
    filter_type = models.CharField(verbose_name="响应过滤类型", max_length=55, choices=RESPONSE_FILTER_TYPES)
    response = models.TextField(blank=True, verbose_name=u"响应内容")
    # 注意 进行策略下发后 反馈 一定是这里的responce定义格式的模板
    add_time = models.DateTimeField(auto_now_add=True, verbose_name="下发时间")

    def __str__(self):
        return self.policyaction.action_name + "-下发"

    class Meta:
        db_table = "action_history"
        verbose_name = "策略下发执行历史"
        ordering = ('-add_time',)


# 策略规则，就是规则的内容
class PolicyRule(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    belong_cop = models.ForeignKey(SysManagerCopInfo, verbose_name="部件应用", on_delete=models.CASCADE, related_name="policy_rule_cop")
    policy_bench = models.ForeignKey(PolicyBench, verbose_name="策略基准", on_delete=models.CASCADE, related_name="policy_bench_rule")
    plat_username = models.CharField(max_length=255, verbose_name="关联的平台用户", blank=True)
    active = models.BooleanField(verbose_name="生效", default=True)

    policy_action = models.ForeignKey(PolicyAction, verbose_name="规则执行指定", on_delete=models.CASCADE, related_name="policy_rule_cop")
    add_time = models.DateTimeField(auto_now_add=True, verbose_name="创建日期")

    def __str__(self):
        return "基于【" + self.policy_bench.name + "】的规则"

    class Meta:
        db_table = "policy_rule"
        verbose_name = "策略规则"
        ordering = ('-add_time',)

## 安全机制;
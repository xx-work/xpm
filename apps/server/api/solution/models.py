from django.db import models
import uuid


from ..xobj.models import SysManagerCopInfo

# from services.models import UserProfile
InfoSecEventTypes = (
    ('attack', '攻击事件'),
    ('bug', '故障事件'),
    ('destory', '灾害事件'),
)

InfoSecEventlevels = (
    (1, '一般'),
    (2, '重大'),
    (3, '特别重大'),
)

negative_impacts = ["违背保密性(未授权泄露)", "违背完整性(未授权篡改)", "违背可用性(即不可用)", "违背抗抵赖性", "遭受破坏"]
attacker_descs = ["犯罪/经济利益", "消遣/黑客攻击", "政治/恐怖主义", "报复", "其他"]


class EffectInfo(models.Model):
    negative_impact =  models.CharField(max_length=100, verbose_name="负面影响")

    @staticmethod
    def inital():
        EffectInfo.objects.all().delete()
        EffectInfo.objects.bulk_create([EffectInfo(negative_impact=x) for x in negative_impacts])

    class Meta:
        db_table="negative_impact"
        verbose_name="负面影响"


class AttackerActionDesc(models.Model):
    attacker_desc = models.CharField(max_length=100, verbose_name="攻击者描述")

    @staticmethod
    def inital():
        AttackerActionDesc.objects.all().delete()
        AttackerActionDesc.objects.bulk_create([AttackerActionDesc(attacker_desc=x) for x in attacker_descs])

    class Meta:
        db_table = "attacker_action_desc"
        verbose_name = "攻击者行为描述"


class InfoSecEvent(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    descover_time = models.DateTimeField(verbose_name="发现时间")
    happend_time = models.DateTimeField(verbose_name="事件发生时间")
    report_time = models.DateTimeField(verbose_name="报告时间", auto_now_add=True)
    reporter = models.CharField(max_length=100, verbose_name="报告提交者用户名")
    infosysname = models.CharField(max_length=100, verbose_name="信息系统名称")
    describtion = models.TextField(verbose_name="信息描述")
    info_type = models.CharField(choices=InfoSecEventTypes, default='attack', max_length=50)
    info_level = models.IntegerField(choices=InfoSecEventlevels, default=1)

    impact_cops = models.ManyToManyField(SysManagerCopInfo, verbose_name="受影响的资产列表", related_name="info_conn_cops")
    negative_impacts = models.ManyToManyField(AttackerActionDesc, verbose_name="攻击者行为描述", related_name="info_conn_attack")
    attacker_descs = models.ManyToManyField(SysManagerCopInfo, verbose_name="负面影响列表", related_name="info_conn_impact")
    impact_area = models.CharField(choices=InfoSecEventTypes, default='Guest', max_length=50)

    had_action = models.TextField(verbose_name="已经采取的行动", blank=True)
    plan_action = models.TextField(verbose_name="计划采取的行动", blank=True)

    class Meta:
        db_table="infosec_event"
        verbose_name="信息事件"

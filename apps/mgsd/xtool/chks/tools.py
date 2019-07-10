from mgsd.models import InfoSecEvent, SysManagerCopInfo
from mgsd.api.solution.models import AttackerActionDesc, EffectInfo


def user_chk_2_infosec(user):
    _info = InfoSecEvent(
        descover_time=user.date_created,
        happend_time=user.date_created,
        reporter='admin007',
        # info_source=None,
        infosysname='增加管理用户-[' + user.name + ']',
        describtion='系统管理部件接入，检查是否是正常接入。',
        info_type='bug',
        info_level=2,
        plat_etype='security',
        info_source=SysManagerCopInfo.objects.get(uniq_flag='cya_cso_6000_v1'),
        plan_action='上报对应的措施到系统管理员，进行接入设置的相关管理。',
        extra='ConnectManagerUserInfo.{}'.format(user.id)
    )
    _info.save()
    _info.negative_impacts.add(AttackerActionDesc.objects.get(attacker_desc='其他'))
    _info.effect_info.add(EffectInfo.objects.get(negative_impact='违背可用性(即不可用)'))
    return True


def cop_chk_2_infosec(cop):
    _info = InfoSecEvent(
        descover_time=cop.date_created,
        happend_time=cop.date_created,
        reporter='admin007',
        # info_source=cop,
        infosysname='增加系统管理部件的接入-[' + cop.name + ']',
        describtion='系统管理部件接入，检查是否是正常接入。',
        info_type='bug',
        info_level=2,
        plat_etype='system',
        info_source=SysManagerCopInfo.objects.get(uniq_flag='cya_cso_6000_v1'),
        # had_action = models.TextField(verbose_name="已经采取的行动", blank=True)
        plan_action='上报对应的措施到系统管理员，进行接入设置的相关管理。',
        extra='SysManagerCopInfo.{}'.format(cop.id)
    )
    _info.save()
    _info.negative_impacts.add(AttackerActionDesc.objects.get(attacker_desc='其他'))
    _info.effect_info.add(EffectInfo.objects.get(negative_impact='违背可用性(即不可用)'))


def aud_chk_2_infosec(alog):
    _info = InfoSecEvent(
        descover_time=alog.date_created,
        happend_time=alog.date_created,
        reporter='admin007',
        # info_source=None,
        infosysname='增加审计对象-[' + alog.name + ']',
        describtion='审计对象接入，检查是否是正常接入。',
        info_type='bug',
        info_level=2,
        plat_etype='audit',
        info_source=SysManagerCopInfo.objects.get(uniq_flag='cya_cso_6000_v1'),
        # had_action = models.TextField(verbose_name="已经采取的行动", blank=True)
        plan_action='上报对应的措施到系统管理员，进行接入设置的相关管理。',
        extra='AuditLogObject.{}'.format(alog.id)
    )
    _info.save()
    _info.negative_impacts.add(AttackerActionDesc.objects.get(attacker_desc='其他'))
    _info.effect_info.add(EffectInfo.objects.get(negative_impact='违背可用性(即不可用)'))
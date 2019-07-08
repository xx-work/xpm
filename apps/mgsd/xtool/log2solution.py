
from mgsd.api.solution.models import InfoSecEventTypes, InfoSecEvent, InfoEventStates, \
    InfoSecEventlevels, PolicyBaseTypes, AttackerActionDesc, EffectInfo


def log_audit_to_solution(_object):
    """

    :param _object: 预备参与审计管理的对象。都没有接入。
    :return:
    """
    pass


def demo_cop_render():
    from mgsd.models import SysManagerCopInfo

    cops = SysManagerCopInfo.objects.all()
    for cop in cops:
        _info = InfoSecEvent(
            descover_time=cop.date_created ,
            happend_time=cop.date_created,
            reporter='admin007',
            # info_source=cop,
            infosysname='增加系统管理部件的接入-[' + cop.name + ']',
            describtion='系统管理部件接入',
            info_type='bug',
            info_level=2,
            plat_etype='system',
            # had_action = models.TextField(verbose_name="已经采取的行动", blank=True)
            plan_action='上报对应的措施到系统管理员，进行接入设置的相关管理。'
        )
        _info.savse()
        _info.negative_impacts.add(AttackerActionDesc.objects.get(attacker_desc='其他'))
        _info.effect_info.add(EffectInfo.objects.get(negative_impact='违背可用性(即不可用)'))


def demo_user_render():
    from mgsd.models import ConnectManagerUserInfo

    users = ConnectManagerUserInfo.objects.all()
    for user in users:
        _info = InfoSecEvent(
            descover_time=user.date_created ,
            happend_time=user.date_created,
            reporter='admin007',
            # info_source=None,
            infosysname='增加管理用户-[' + user.name + ']',
            describtion='系统管理部件接入',
            info_type='bug',
            info_level=2,
            plat_etype='audit',
            # had_action = models.TextField(verbose_name="已经采取的行动", blank=True)
            plan_action='上报对应的措施到系统管理员，进行接入设置的相关管理。'
        )
        _info.save()
        _info.negative_impacts.add(AttackerActionDesc.objects.get(attacker_desc='其他'))
        _info.effect_info.add(EffectInfo.objects.get(negative_impact='违背可用性(即不可用)'))


def demo_audit_render():
    from mgsd.models import ConnectManagerUserInfo

    users = ConnectManagerUserInfo.objects.all()
    for user in users:
        _info = InfoSecEvent(
            descover_time=user.date_created ,
            happend_time=user.date_created,
            reporter='admin007',
            # info_source=None,
            infosysname='增加管理用户-[' + user.name + ']',
            describtion='系统管理部件接入',
            info_type='bug',
            info_level=2,
            plat_etype='audit',
            # had_action = models.TextField(verbose_name="已经采取的行动", blank=True)
            plan_action='上报对应的措施到系统管理员，进行接入设置的相关管理。'
        )
        _info.save()
        _info.negative_impacts.add(AttackerActionDesc.objects.get(attacker_desc='其他'))
        _info.effect_info.add(EffectInfo.objects.get(negative_impact='违背可用性(即不可用)'))







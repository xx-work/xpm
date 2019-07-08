
from mgsd.api.solution.models import InfoSecEventTypes, InfoSecEvent, InfoEventStates, InfoSecEventlevels, PolicyBaseTypes


def log_audit_to_solution(_object):
    """

    :param _object: 预备参与审计管理的对象。都没有接入。
    :return:
    """
    pass


def demo_content_render():
    from mgsd.models import SysManagerCopInfo

    cops = SysManagerCopInfo.objects.all()

    for cop in cops:
        _info = InfoSecEvent(
            descover_time=cop.date_created ,
            happend_time=cop.date_created,
            reporter='admin007',
            info_source=cop,
            infosysname='增加系统管理部件的接入-[' + cop.name + ']',
            describtion='系统管理部件接入',
            info_type='bug',
            info_level=2,
            plat_etype='system',
            # had_action = models.TextField(verbose_name="已经采取的行动", blank=True)
            plan_action='上报对应的措施到'
        )




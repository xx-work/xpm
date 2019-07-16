# coding:utf-8
import rsa

from mgsd.api.xobj.models import SysManagerCopInfo, ConnectManagerUserInfo
from mgsd.api.solution.models import InfoSecEvent, InfoSecEventlevels, InfoEventStates, InfoSecEventTypes, EffectInfo, AttackerActionDesc

POT_USERNAME = 'pot001'
POT_IP = '192.168.2.175'
IV = '1q2w3e4R'.encode('UTF-8')


def load_cop_user(auth_username=POT_USERNAME, auth_passwd='QDF==12@##$FSD*(DF****'):
    if auth_username not in [x.username for x in ConnectManagerUserInfo.objects.all() ]:
        pot_alert_connect_user = ConnectManagerUserInfo.objects.create(
            username=auth_username, _password=auth_passwd
        )
    else:
        pot_alert_connect_user = ConnectManagerUserInfo.objects.get(username=auth_username)

    # 签发keys
    if not pot_alert_connect_user._private_key or not pot_alert_connect_user._public_key:
        pubkey, privkey = rsa.newkeys(1024)
        pot_alert_connect_user._private_key=privkey
        pot_alert_connect_user._public_key=pubkey
        pot_alert_connect_user.save()

    return pot_alert_connect_user


def inital_pots_coper(srouce_ip=POT_IP, auth_username=POT_USERNAME, auth_passwd='QDF==12@##$FSD*(DF****'):
    """
    初始化蜜罐部件管理系统
    :return:
    """
    # 创建蜜罐用户

    pot_alert_connect_user = load_cop_user(auth_username, auth_passwd)
    # 加载蜜罐部件
    try:
        pot_copers = SysManagerCopInfo.objects.filter(ip=srouce_ip)
        pot_coper = pot_copers[0]
        if not pot_coper.managers:
            pot_coper.managers.add(pot_alert_connect_user)
    except:
        pot_coper = SysManagerCopInfo(
            uniq_flag='cya_pot_C6000_v1', name='蜜罐', ip = srouce_ip,
        type='Others', level='High', pushed=True, os ='Centos:7.4',
        mac='-', mac_vendor='CYA', up=True, extra='Others',)
        pot_coper.save()
        pot_coper.managers.add(pot_alert_connect_user)
    return pot_coper


from datetime import datetime
_now = datetime.now()


def pot2cso(descover_time=str(_now), happend_time=str(_now),
            infosysname='test_input', extra='无补充信息', summary='', advice='',
            auth_username=POT_USERNAME, auth_passwd='*#$!!!FDF#322'):
    """

    :param remote_addr:
    :param descover_time: 发现时间
    :param happend_time: 发生时间
    :param infosysname: 告警名称
    :param extra:  额外信息
    :param summary: 告警描述
    :param advice: 告警建议; 计划措施
    :param auth_username: 连接用户名 pot001
    :param auth_passwd: 连接密码 112233..
    :return: flug, obj
    """
    _local_cop = inital_pots_coper(srouce_ip=POT_IP, auth_username=auth_username, auth_passwd=auth_passwd)
    _info = InfoSecEvent(
        descover_time=descover_time if descover_time else str(_now),
        happend_time=happend_time if happend_time else str(_now),
        reporter=auth_username,
        info_source=_local_cop,
        infosysname=infosysname if infosysname else '-',
        extra=extra if extra else '-',
        describtion=summary if summary else '-',
        info_type='attack',
        info_level='3',
        plan_action=advice if advice else '-'
    )
    _info.save()
    _info.impact_cops.add(_local_cop)
    _info.negative_impacts.add(AttackerActionDesc.objects.get(attacker_desc='其他'))
    _info.effect_info.add(EffectInfo.objects.get(negative_impact="遭受破坏"))

    return True, _info

from rsa import PublicKey, PrivateKey


def user_sig_is_ture(_public_key, sig, IV=IV):
    exec('public = {}'.format(_public_key))

    # slug = rsa.verify(message=IV, signature=sig, pub_key=locals()['public'])
    # return slug == 'SHA-1'

    try:

        slug = rsa.verify(message=IV, signature=sig, pub_key=locals()['public'])
        return slug=='SHA-1'
    except:
        return False
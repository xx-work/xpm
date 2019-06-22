from __future__ import absolute_import

from collections import OrderedDict
from django.apps import apps
from xadmin.util import smart_text, capfirst, sortkeypicker
from xadmin.plugins.inline import Inline, filter_hook
import xadmin
from xadmin import views
# from xadmin.layout import Main, TabHolder, Tab, Fieldset, Row, Col, AppendedText, Side
# from xadmin.plugins.batch import BatchChangeAction
from django.contrib.auth.models import Group, User, Permission


from reversion.models import Revision
from xadmin.models import Log


from server.api.center.models import SystemPolicyCentralizedManagement, AuditPolicyCentralizedManagement, SecurityPolicyCentralizedManagement
from server.api.xobj.models import SysManagerCopInfo, ConnectManagerUserInfo, AuditLogObject
from server.api.policy.models import PolicyActionHistory, PolicyRule, PolicyAction, PolicyBench
from server.api.monitor.models import ObjProcess, ProcessAuditLog
from server.api.solution.models import InfoSecEvent, InfoGoin, AttackerActionDesc, EffectInfo
from server.api.chk.models import ChangeAudit
from server.api.backer.models import BackUpHistory

from agent.snmpd.models import SnmpAgentCfgInfo, SnmpHostData
from services.models import Community

from django_celery_beat.models import PeriodicTask, IntervalSchedule, CrontabSchedule


@xadmin.sites.register(views.CommAdminView)
class GlobalSetting(object):
    site_title = '信息系统安全管理平台'  # 头部系统名称
    # menu_style = 'accordion'  # 设置数据管理导航折叠，以每一个app为一个折叠框

    menu_style = 'accordion'  # 'accordion'  default
    site_footer = 'COPYRIGHT © 2010 - 2018 ALL RIGHTS RESERVED"'  # 底部版权
    # menu_style = 'accordion'  # 设置数据管理导航折叠，以每一个app为一个折叠框

    global_search_models = [PolicyRule]
    global_models_icon = {
        SysManagerCopInfo: "fa fa-laptop", SystemPolicyCentralizedManagement: "fa fa-cloud"
    }

    # http://www.fontawesome.com.cn/faicons/
    def get_site_menu(self):
        return (
            {'title': '策略集中管理', 'menus': (
                {'title': '系统策略集中管理', 'url': self.get_model_url(SystemPolicyCentralizedManagement, 'changelist')},
                {'title': '安全策略集中管理', 'url': self.get_model_url(SecurityPolicyCentralizedManagement, 'changelist')},
                {'title': '审计策略集中管理', 'url': self.get_model_url(AuditPolicyCentralizedManagement, 'changelist')},
            ), "icon": "fa fa-heart"},

            {'title': '管理对象识别', 'menus': (
                {'title': '系统管理对象识别', 'url': self.get_model_url(SysManagerCopInfo, 'changelist')},
                {'title': '安全管理对象识别', 'url': self.get_model_url(ConnectManagerUserInfo, 'changelist')},
                {'title': '审计机制对象', 'url': self.get_model_url(AuditLogObject, 'changelist')},
            ), "icon": "fa fa-html5"},

            {'title': '管理策略设置', 'menus': (
                {'title': '管理策略基准', 'url': self.get_model_url(PolicyBench, 'changelist')},
                {'title': '管理策略规则', 'url': self.get_model_url(PolicyRule, 'changelist')},
                {'title': '管理规则下发', 'url': self.get_model_url(PolicyAction, 'changelist')},
            ), "icon": "fa fa-cog"},

            {'title': '运行监控', 'menus': (
                {'title': '运行进程监控', 'url': self.get_model_url(ObjProcess, 'changelist')},
                {'title': '运行基本参数监控', 'url': self.get_model_url(SnmpHostData, 'changelist')},

            ), "icon": "fa fa-eye"},

            {'title': '事件响应处置', 'menus': (
                {'title': '响应处置', 'url': self.get_model_url(InfoSecEvent, 'changelist')},
            ), "icon": "fa fa-adn"},

            {'title': '变更处理', 'menus': (
                {'title': '系统变更处理', 'url': self.get_model_url(ChangeAudit, 'changelist')},
                {'title': '平台操作日志', 'url': self.get_model_url(Log, 'changelist')},
                        ), "icon": "fa fa-try"},

            {'title': '灾难备份和恢复管理', 'menus': (
                {'title': '灾难备份和恢复管理', 'url': self.get_model_url(BackUpHistory, 'changelist')},
            ), "icon":"fa fa-user"},

            {'title': '安全机制统一管理', 'menus': (
                {'title': '平台用户', 'url': self.get_model_url(User, 'changelist'), "icon":"fa fa-user"},
                {'title': '平台用户组', 'url': self.get_model_url(Group, 'changelist'), "icon":"fa fa-group"},
                {'title': '平台用户权限对象', 'url': self.get_model_url(Permission, 'changelist'), "icon":"fa fa-eject"},
                {'title': '责任管理', 'url': self.get_model_url(Community, 'changelist'), "icon":"fa fa-rocket"},
            ), "icon": "fa fa-users"},

            {'title': '', 'menus': (
            ), "icon": "fa fa-ignore"},

            {'title': '其他工具', 'menus': (
                {'title': 'SNMP设置', 'url': self.get_model_url(SnmpAgentCfgInfo, 'changelist')},
                {'title': '策略下发记录', 'url': self.get_model_url(PolicyActionHistory, 'changelist')},
                {'title': '进程监控记录', 'url': self.get_model_url(ProcessAuditLog, 'changelist')},
                {'title': '事件跟进记录', 'url': self.get_model_url(InfoGoin, 'changelist')},
            ), "icon": "fa fa-bell"},

            {'title': '响应事件管理设置', 'menus': (
                {'title': '攻击者行为', 'url': self.get_model_url(AttackerActionDesc, 'changelist')},
                {'title': '事件性质管理', 'url': self.get_model_url(EffectInfo, 'changelist')},
                # {'title': '事件跟进记录', 'url': self.get_model_url(InfoGoin, 'changelist')},
            ), "icon": "fa fa-users"},


            {'title': '', 'menus': (), "icon": "fa fa-ignore"},

            {'title': '平台版本更新记录', 'menus': (
                {'title': '版本更新', 'url': self.get_model_url(Revision, 'changelist')},
               ), "icon": "fa fa-fire"},

        )

# """
# select user_alert.*, regular.rules_type, regular.msg from
# (select rule_id, count(rule_id) as c from user_alert where start_time between '2019-5-1' and '2019-6-1' group by rule_id
# order by c desc) as user_alert  left join regular on user_alert.rule_id=regular.sid limit 10
# """
#
#
# """
# select src_ip, count(src_ip) as c from user_alert where start_time between '2019-5-1' and '2019-6-1' group by src_ip order by c desc''
#
# """
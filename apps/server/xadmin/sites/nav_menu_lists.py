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

from server.models import SnmpHostData, SystemPolicyCentralizedManagement,\
    SnmpAgentCfgInfo, SystemObjProcess, InfoSecEvent, SysManagerCopInfo, EffectInfo, ChangeAudit, \
    ConnectManagerUserInfo, BackUpHistory, AttackerActionDesc, PolicyRule, PolicyBench, PolicyAction


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
                {'title': '系统策略集中管理', 'url': self.get_model_url(SystemPolicyCentralizedManagement, 'changelist'), "icon":"fa fa-home"},
                {'title': '安全策略集中管理', 'url': self.get_model_url(SystemPolicyCentralizedManagement, 'changelist'), "icon":"fa fa-home"},
                {'title': '审计策略集中管理', 'url': self.get_model_url(SystemPolicyCentralizedManagement, 'changelist'), "icon":"fa fa-home"},
            ), "icon":"fa fa-heart"},

            {'title': '管理对象识别', 'menus': (
                {'title': '系统管理对象识别', 'url': self.get_model_url(SysManagerCopInfo, 'changelist')},
                {'title': '安全管理对象识别', 'url': self.get_model_url(ConnectManagerUserInfo, 'changelist')},
                # {'title': '审计机制对象', 'url': self.get_model_url(ScanRecode, 'changelist')},
            )},

            {'title': '管理策略设置', 'menus': (
                {'title': '管理策略基准', 'url': self.get_model_url(PolicyBench, 'changelist')},
                {'title': '管理策略规则', 'url': self.get_model_url(PolicyRule, 'changelist')},
                {'title': '管理规则下发', 'url': self.get_model_url(PolicyAction, 'changelist')},
            ), "icon":"fa fa-certificate"},

            {'title': '运行监控', 'menus': (
                {'title': '系统部件运行监控', 'url': self.get_model_url(SystemObjProcess, 'changelist')},
                {'title': '安全机制运行监控', 'url': self.get_model_url(SystemObjProcess, 'changelist')},
                {'title': '审计机制运行监控', 'url': self.get_model_url(SystemObjProcess, 'changelist')},
            ), "icon":"fa fa-book"},

            {'title': '事件响应处置', 'menus': (
                {'title': '系统事件响应处置', 'url': self.get_model_url(InfoSecEvent, 'changelist')},
                {'title': '安全事件响应处置', 'url': self.get_model_url(InfoSecEvent, 'changelist')},
                {'title': '审计事件响应处置', 'url': self.get_model_url(InfoSecEvent, 'changelist')},
            ), "icon": "fa fa-book"},

            {'title': '系统变更处理', 'menus': (
                {'title': '系统变更处理', 'url': self.get_model_url(ChangeAudit, 'changelist')},
                        ), "icon":"fa fa-book"},

            {'title': '灾难备份和恢复管理', 'menus': (
                {'title': '灾难备份和恢复管理', 'url': self.get_model_url(BackUpHistory, 'changelist')},
            ), "icon":"fa fa-user"},

            {'title': '安全机制统一管理', 'menus': (
                {'title': '平台用户', 'url': self.get_model_url(User, 'changelist')},
                {'title': '平台用户组', 'url': self.get_model_url(Group, 'changelist')},
                {'title': '平台用户权限对象', 'url': self.get_model_url(Permission, 'changelist')},
            ), "icon": "fa fa-user"}
        )

from __future__ import absolute_import

import xadmin
from xadmin import views
try:
    from django.core.urlresolvers import reverse
except:
    from django.urls import reverse


from mgsd.api.xobj.models import SysManagerCopInfo, ConnectManagerUserInfo, AuditLogObject
from mgsd.api.policy.models import PolicyActionHistory, PolicyRule, PolicyAction, PolicyBench
from mgsd.api.monitor.models import ObjProcess, ProcessAuditLog
from mgsd.api.solution.models import InfoSecEvent, InfoGoin, AttackerActionDesc, EffectInfo
from mgsd.api.chk.models import ChangeAudit
from mgsd.api.backer.models import BackUpHistory


from secs.api.oauth.models import Community
from django.contrib.auth.models import User, Group, Permission

from ...url_confs import get_menu_url

# 全部都是补丁模板
from mgsd.api.models import SystemPolicyCentralizedManagement, SecurityPolicyCentralizedManagement, AuditPolicyCentralizedManagement
from mgsd.models import SecurityPolicyRule, AuditPolicyRule, SystemPolicyRule
from mgsd.models import AuditChangeAudit, SecurityChangeAudit, SystemChangeAudit
from mgsd.models import SecurityEventResponseSolve, SystemEventResponseSolve, AuditEventResponseSolve


@xadmin.sites.register(views.CommAdminView)
class GlobalSetting(object):
    site_title = '信息系统安全管理平台'  # 头部系统名称
    # menu_style = 'accordion'  # 设置数据管理导航折叠，以每一个app为一个折叠框

    menu_style = 'accordion'  # 'accordion'  default
    site_footer = 'COPYRIGHT © 2010 - 2018 ALL RIGHTS RESERVED"'  # 底部版权
    # menu_style = 'accordion'  # 设置数据管理导航折叠，以每一个app为一个折叠框

    global_search_models = [PolicyRule]

    # http://www.fontawesome.com.cn/faicons/
    def get_site_menu(self):

        return (
                {'title': '安全策略及安全责任管理', 'menus': (
                    {'title': '组织机构角色责任和权限管理', 'url': self.get_model_url(Community, 'changelist'), },
                    {'title': '组织的安全和管理', 'url': self.get_model_url(Permission, 'changelist'), },
                    {'title': '组织的信息安全责任制度管理', 'url': self.get_model_url(Group, 'changelist'), },
                    {'title': '平台管理员用户管理', 'url': self.get_model_url(User, 'changelist'), },
                    {'title': '平台管理员安全责任管理', 'url': "/admin/6", },

                ), "icon": "fa fa-heart"},

                {'title': '系统部件管理', 'menus': (
                    {'title': '系统策略集中管理', 'url': self.get_model_url(SystemPolicyCentralizedManagement, 'changelist') },
                    {'title': '系统管理对象识别', 'url': self.get_model_url(SysManagerCopInfo, 'changelist')},
                    {'title': '系统管理策略设置', 'url': self.get_model_url(SystemPolicyRule, 'changelist')},
                    {'title': '系统部件运行监控', 'url': '/fffffffffffffffff'},
                    {'title': '系统事件响应处置', 'url': self.get_model_url(SystemEventResponseSolve, 'changelist')},
                    {'title': '系统变更管理', 'url':  self.get_model_url(SystemChangeAudit, 'changelist')},
                    {'title': '灾难备份及恢复管理', 'url': self.get_model_url(BackUpHistory, 'changelist')},
                ), "icon": "fa fa-html5"},

                {'title': '安全机制管理', 'menus': (
                    {'title': '安全策略集中管理', 'url': self.get_model_url(SecurityPolicyCentralizedManagement, 'changelist')},
                    {'title': '安全管理对象识别', 'url': self.get_model_url(ConnectManagerUserInfo, 'changelist')},
                    {'title': '安全管理策略设置', 'url':  self.get_model_url(SecurityPolicyRule, 'changelist')},
                    {'title': '安全机制审计监控', 'url':  '/fdafdsafds'},
                    {'title': '安全事件响应处置', 'url': self.get_model_url(SecurityEventResponseSolve, 'changelist')},
                    {'title': '安全变更管理', 'url': self.get_model_url(SecurityChangeAudit, 'changelist')},
                ), "icon": "fa fa-cog"},

                {'title': '审计机制管理', 'menus': (
                    {'title': '审计策略集中管理', 'url': self.get_model_url(AuditPolicyCentralizedManagement, 'changelist')},
                    {'title': '审计管理对象识别', 'url': self.get_model_url(AuditLogObject, 'changelist')},
                    {'title': '审计管理策略设置', 'url': self.get_model_url(AuditPolicyRule, 'changelist')},
                    {'title': '审计机制运行监控', 'url': '/234232ewr'},
                    {'title': '审计事件响应处置', 'url': self.get_model_url(AuditEventResponseSolve, 'changelist')},
                    {'title': '审计变更管理', 'url': self.get_model_url(AuditChangeAudit, 'changelist') },
                ), "icon": "fa fa-eye"},

                {'title': '数据管理功能', 'menus': (
                    {'title': '数据策略集中管理', 'url': '/11', },
                    {'title': '数据分类', 'url': '/12', },
                    {'title': '数据存储', 'url': '/13', },
                    {'title': '数据应用', 'url': '/14', },
                    {'title': '信息可视化管理', 'url': '/15', },
                ), "icon": "fa fa-adn"},

                {'title': '接口功能', 'menus': (
                    {'title': '平台接口集中管理', 'url': '/31', },
                    {'title': '面向对象接口', 'url': '/122', },
                    {'title': '平台操作人机接口', 'url': '/123', },
                    {'title': '平台级联接口', 'url': '/142', },
                    {'title': '扩展功能接口', 'url': '/152', },
                ), "icon": "fa fa-adn"},
            )



from .views.custom_view import SystemCentralManagementsView, TestEchartsView, TestBootstrapTableView


xadmin.site.register_view(r'sys_center_m$', SystemCentralManagementsView, name='sys_center_m')
xadmin.site.register_view(r'test_echarts', TestEchartsView, name='test_echarts')
# xadmin.site.register_view(r'test_bootstrp_table$', TestBootstrapTableView, name='test_bootstrp_table')


from xadmin.views import BaseAdminPlugin, CreateAdminView, ModelFormAdminView, UpdateAdminView, ListAdminView
from mgsd.xadmin.plugins.tplugin import ListReturndPlugin
xadmin.site.register_plugin(ListReturndPlugin, ListAdminView)
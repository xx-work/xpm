from __future__ import absolute_import

from collections import OrderedDict
from django.apps import apps
from xadmin.util import smart_text, capfirst, sortkeypicker
from xadmin.plugins.inline import Inline, filter_hook

import xadmin
from xadmin import views
from xadmin.layout import Main, TabHolder, Tab, Fieldset, Row, Col, AppendedText, Side
from xadmin.plugins.inline import Inline
from xadmin.plugins.batch import BatchChangeAction

from ..models import SysManagerCopInfo, PolicyRule


# @xadmin.sites.register(views.website.IndexView)
# class MainDashboard(object):
#     widgets = [
#         [
#             {"type": "html", "title": "首页设置窗体",
#              "content": "<h3> 信息系统安全管理平台 </h3><p> GB∕T 34990-2017 信息安全技术 信息系统安全管理平台技术要求和测试评价方法 </p>"},
#             {"type": "list", "model": "server.SysManagerCopInfo", "params": {"o": "-date_updated"}},
#         ],
#         [
#             {"type": "qbutton", "title": "管理部件和策略",
#              "btns": [{"model": SysManagerCopInfo},
#                       {"model": PolicyRule},
#                       ]},
#             {"type": "addform", "model": SysManagerCopInfo},
#         ]
#     ]


@xadmin.sites.register(views.BaseAdminView)
class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


from .sites.nav_menu_lists import GlobalSetting
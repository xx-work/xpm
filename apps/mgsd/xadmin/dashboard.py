from __future__ import absolute_import

# from collections import OrderedDict
# from django.apps import apps
# from xadmin.util import smart_text, capfirst, sortkeypicker
# from xadmin.plugins.inline import Inline, filter_hook

import xadmin
from xadmin import views
# from xadmin.layout import Main, TabHolder, Tab, Fieldset, Row, Col, AppendedText, Side
# from xadmin.plugins.inline import Inline
# from xadmin.plugins.batch import BatchChangeAction
#
# from ..models import SysManagerCopInfo, PolicyRule


# @xadmin.sites.register(views.website.IndexView)
# class MainDashboard(object):
#     title = u"信息系统安全管理平台"
#     icon = "fa fa-dashboard"
#
#     def get_page_id(self):
#         return 'sys_center_m'


@xadmin.sites.register(views.BaseAdminView)
class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


from .sites.nav_menu_lists import GlobalSetting
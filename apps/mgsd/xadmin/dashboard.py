from __future__ import absolute_import


import xadmin
from xadmin import views

# @xadmin.sites.register(views.website.IndexView)
# class MainDashboard(object):
#     title = u"信息系统安全管理平台"
#     icon = "fa fa-dashboard"
#
#     def get_page_id(self):
#         return 'sys_center_m'


@xadmin.sites.register(views.BaseAdminView)
class BaseSetting(object):
    enable_themes = False
    use_bootswatch = False


# from .sites.nav_menu_lists import GlobalSetting


# 2019-6-27 修改为新的结构
from .sites.nav_v2 import GlobalSetting
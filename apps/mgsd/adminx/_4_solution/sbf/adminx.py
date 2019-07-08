# coding:utf-8

from __future__ import absolute_import

import xadmin

from ....api.models import ConnectManagerUserInfo, ChangeAudit, SysManagerCopInfo
from ....api.solution.models import InfoSecEvent, InfoSecEventTypes
from ....api.none4cso.models import SystemEventResponseSolve, AuditEventResponseSolve, SecurityEventResponseSolve


from xadmin.views import ListAdminView
from mgsd.api.chk.models import PolicyBaseTypes

from mgsd.xadmin.utils.self_utils import get_markd_table_details_show


class SystemEventResponseSolveAdmin(ListAdminView):
    show_bookmarks = False
    list_display_links = None

    remove_permissions = ['add', 'change', 'delete']

    def get_report_user(self, instance):
        plat_user = ConnectManagerUserInfo.objects.get(username=instance.reporter)
        return get_markd_table_details_show(
            url=self.get_model_url(ConnectManagerUserInfo, 'changelist', ) + "{id}/detail/".format(
                id=plat_user.id), title=plat_user.name)
    get_report_user.short_description = "报告用户"

    def get_report_name(self, instance):
        return instance.infosysname
    get_report_name.short_description = "事件名"

    def get_report_time(self, instance):
        return instance.report_time
    get_report_time.short_description = "报告名"

    def get_change_obj(self, instance):
        return instance.change_obj
    get_change_obj.short_description = "变更对象"

    def get_describtion(self, instance):
        return instance.describtion
    get_describtion.short_description = "事件描述"

    def get_info_level(self, instance):
        return instance.info_level
    get_info_level.short_description = "事件等级"

    def get_detailed_show(self, instance):
        return get_markd_table_details_show(self.get_model_url(InfoSecEvent, 'changelist') + str(instance.id) + "/detail/", title='详情')
    get_detailed_show.short_description = "事件详情"

    list_display = ['get_report_name', 'get_change_obj', 'get_info_level', 'get_report_time', 'get_describtion', 'get_detailed_show']

    def queryset(self):
        qs = InfoSecEvent.objects.filter(plat_etype=PolicyBaseTypes[0][0], info_type=InfoSecEventTypes[1][0])
        return qs


class SecurityEventResponseSolveAdmin(SystemEventResponseSolveAdmin):
    def queryset(self):
        qs = InfoSecEvent.objects.filter(plat_etype=PolicyBaseTypes[1][0], info_type=InfoSecEventTypes[1][0])
        return qs


class AuditEventResponseSolveAdmin(SystemEventResponseSolveAdmin):
    def queryset(self):
        qs = InfoSecEvent.objects.filter(plat_etype=PolicyBaseTypes[2][0], info_type=InfoSecEventTypes[1][0])
        return qs


xadmin.site.register(SystemEventResponseSolve, SystemEventResponseSolveAdmin)
xadmin.site.register(SecurityEventResponseSolve, SecurityEventResponseSolveAdmin)
xadmin.site.register(AuditEventResponseSolve, AuditEventResponseSolveAdmin)


# coding:utf-8

from __future__ import absolute_import

import xadmin

from ....api.models import ConnectManagerUserInfo, ChangeAudit

from ....api.none4cso.models import SystemChangeAudit, AuditChangeAudit, SecurityChangeAudit

from xadmin.views import ListAdminView
from mgsd.api.chk.models import PolicyBaseTypes

from mgsd.xadmin.utils.self_utils import get_markd_table_details_show


class SystemChangeAuditAdmin(ListAdminView):
    show_bookmarks = False
    list_display_links = None

    remove_permissions = ['add', 'change', 'delete']

    def get_chk_user(self, instance):
        plat_user = ConnectManagerUserInfo.objects.get(username=instance.opreate_username)
        return get_markd_table_details_show(
            url=self.get_model_url(ConnectManagerUserInfo, 'changelist', ) + "{id}/detail/".format(
                id=plat_user.id), title=plat_user.name)
    get_chk_user.short_description = "操作用户"

    def get_chanage_stat(self, instance):
        return instance.change_stat
    get_chanage_stat.short_description = "变更状态"

    def get_change_name(self, instance):
        return instance.change_name
    get_change_name.short_description = "变更名"

    def get_change_obj(self, instance):
        return instance.change_obj
    get_change_obj.short_description = "变更对象"

    def get_change_detail(self, instance):
        return instance.change_obj
    get_change_detail.short_description = "变更详情"

    def get_change_time(self, instance):
        return instance.change_name
    get_change_time.short_description = "变更时间"

    list_display = ['get_change_name', 'get_chanage_stat', 'get_change_obj', 'get_change_detail', 'get_change_time']

    def queryset(self):
        qs = ChangeAudit.objects.filter(change_type=PolicyBaseTypes[0][0])
        return qs


class SecurityChangeAuditAdmin(SystemChangeAuditAdmin):
    def queryset(self):
        return ChangeAudit.objects.filter(change_type=PolicyBaseTypes[1][0])


class AuditChangeAuditAdmin(SystemChangeAuditAdmin):
    def queryset(self):
        return ChangeAudit.objects.filter(change_type=PolicyBaseTypes[2][0])


xadmin.site.register(SystemChangeAudit, SystemChangeAuditAdmin)
xadmin.site.register(SecurityChangeAudit, SecurityChangeAuditAdmin)
xadmin.site.register(AuditChangeAudit, AuditChangeAuditAdmin)

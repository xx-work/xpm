# coding:utf-8

from __future__ import absolute_import

import xadmin
from xadmin.views import ListAdminView
from xadmin.models import Log

from ....api.models import ConnectManagerUserInfo, ChangeAudit
from ....api.none4cso.models import SystemChangeAudit, AuditChangeAudit, SecurityChangeAudit
from ....xtool.log2chk import get_chk_recode_by_log

from mgsd.api.chk.models import PolicyBaseTypes
from mgsd.xadmin.utils.self_utils import get_markd_table_details_show, get_detaild_model


class SystemChangeAuditAdmin(ListAdminView):
    show_bookmarks = False
    list_display_links = None
    remove_permissions = ['add', 'change', 'delete']

    def get_chk_user(self, instance):
        plat_user = ConnectManagerUserInfo.objects.get(username=instance.user.username)
        return get_markd_table_details_show(
            url=self.get_model_url(ConnectManagerUserInfo, 'changelist', ) + "{id}/detail/".format(
                id=plat_user.id), title=plat_user.name)
    get_chk_user.short_description = "操作用户"

    def get_chanage_flug(self, instance):
        return instance.action_flag
    get_chanage_flug.short_description = "变更类型"

    def get_change_name(self, instance):
        return get_markd_table_details_show(
            url=self.get_model_url(Log, 'changelist', ) + "{id}/detail/".format(
                id=instance.id), title='变更详情')
    get_change_name.short_description = "变更名"

    def remote_addr(self, instance):
        return instance.ip_addr
    remote_addr.short_description = "访客源"

    def get_change_obj(self, instance):
        ModelObj = instance.content_type.model_class()
        objid = instance.object_id
        return get_markd_table_details_show(url=self.get_model_url(ModelObj, 'changelist')+str(objid)+"/detail/",
                                    title=instance.object_repr)

    get_change_obj.short_description = "变更对象"

    def get_change_detail(self, instance):
        # 字符串
        return instance.object_repr
    get_change_detail.short_description = "变更详情"

    def get_change_time(self, instance):
        return instance.action_time
    get_change_time.short_description = "变更时间"

    def pushed_infosec(self, instance):
        return instance.action_time
    pushed_infosec.short_description = "事件进入处置监督"

    list_display = ['get_change_name', 'get_chanage_flug', 'get_change_obj', 'get_change_detail', 'remote_addr', 'get_change_time', 'pushed_infosec']

    def queryset(self):
        return get_chk_recode_by_log(type=PolicyBaseTypes[0][0])


class SecurityChangeAuditAdmin(SystemChangeAuditAdmin):
    def queryset(self):
        return get_chk_recode_by_log(type=PolicyBaseTypes[1][0])


class AuditChangeAuditAdmin(SystemChangeAuditAdmin):
    def queryset(self):
        return get_chk_recode_by_log(type=PolicyBaseTypes[2][0])


xadmin.site.register(SystemChangeAudit, SystemChangeAuditAdmin)
xadmin.site.register(SecurityChangeAudit, SecurityChangeAuditAdmin)
xadmin.site.register(AuditChangeAudit, AuditChangeAuditAdmin)

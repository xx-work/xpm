import xadmin
from ...api.models import SystemPolicyCentralizedManagement, AuditPolicyCentralizedManagement, SecurityPolicyCentralizedManagement
from xadmin.views import ListAdminView
from .._1_xobj import SysManagerCopInfo, ConnectManagerUserInfo

from ...models import BackUpHistory
from ...xadmin.utils.self_utils import get_markd_table_details_show


# @xadmin.sites.register(SystemPolicyCentralizedManagement)
class SystemPolicyCentralizedManagementAdmin(ListAdminView):
    remove_permissions = ['add', 'change', 'delete']
    show_bookmarks = False
    list_display_links = None

    def cop_self(self, instance):
        return get_markd_table_details_show(
            url=self.get_model_url(SysManagerCopInfo, 'changelist', ) + "{id}/detail/".format(
                id=instance.id), title=str(instance))
    cop_self.short_description = "部件本身"
    cop_self.allow_tags = True
    cop_self.is_column = True

    def cop_state(self, instance):
        return instance.up
    cop_state.short_description = "开启状态"
    cop_state.allow_tags = True
    cop_state.is_column = True

    def backuo2(self, instance):
        _the_last_backed_recodes = BackUpHistory.objects.all().order_by('-date_created')[0]
        return get_markd_table_details_show(self.get_model_url(BackUpHistory, 'changelist') + str(_the_last_backed_recodes.id)
                        + "/detail/", title='最近一次平台备份恢复记录')
    backuo2.short_description = "平台备份恢复记录"

    def logsdump(self, instance):
        _the_last_backed_recodes = BackUpHistory.objects.all().order_by('-date_created')[0]
        return get_markd_table_details_show(self.get_model_url(BackUpHistory, 'changelist') + str(_the_last_backed_recodes.id)
                        + "/detail/", title=str(instance.cop) + '日志备份记录')
    logsdump.short_description = "日志备份记录"

    def cop_connect_user(self, instance):
        from ...xadmin.utils.self_utils import get_detaild_model
        return get_detaild_model(self, ConnectManagerUserInfo, instance.managers.all())

    cop_connect_user.short_description = "部件授权管理员用户集"
    cop_connect_user.allow_tags = True
    cop_connect_user.is_column = True

    list_display = ['cop_self', 'cop_state', 'cop_connect_user','logsdump', 'backuo2']

    def queryset(self):
        qs = SysManagerCopInfo.objects.all()
        return qs


xadmin.site.register(SystemPolicyCentralizedManagement, SystemPolicyCentralizedManagementAdmin)
xadmin.site.register(SecurityPolicyCentralizedManagement, SystemPolicyCentralizedManagementAdmin)
xadmin.site.register(AuditPolicyCentralizedManagement, SystemPolicyCentralizedManagementAdmin)

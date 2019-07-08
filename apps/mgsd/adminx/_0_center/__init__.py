import xadmin
from ...api.models import SystemPolicyCentralizedManagement, AuditPolicyCentralizedManagement, SecurityPolicyCentralizedManagement
from xadmin.views import ListAdminView
from .._1_xobj import SysManagerCopInfo, ConnectManagerUserInfo

from ...models import BackUpHistory
# from ...xadmin.utils.self_utils import get_markd_table_details_show


# @xadmin.sites.register(SystemPolicyCentralizedManagement)
class SystemPolicyCentralizedManagementAdmin(ListAdminView):

    def cop_self(self, instance):
        return instance
    cop_self.short_description = "部件本身"
    cop_self.allow_tags = True
    cop_self.is_column = True

    def cop_state(self, instance):
        return instance.up
    cop_state.short_description = "开启状态"
    cop_state.allow_tags = True
    cop_state.is_column = True

    def backuo2(self, instance):
        from django.utils.safestring import mark_safe
        return mark_safe("""<a data-res-uri="{based_url}" class="details-handler" rel="tooltip" title="{name}"> {name} 
    <i class="fa fa-info-circle"></i> </a>  """.format(based_url=self.get_model_url(BackUpHistory, 'changelist'),
                                                       name='备份记录'))

    backuo2.short_description = "平台备份恢复记录"
    backuo2.allow_tags = True
    backuo2.is_column = True

    def cop_connect_user(self, instance):
        from ...xadmin.utils.self_utils import get_detaild_model
        return get_detaild_model(self, ConnectManagerUserInfo, instance.managers.all())

    cop_connect_user.short_description = "管理员用户集"
    cop_connect_user.allow_tags = True
    cop_connect_user.is_column = True

    list_display = ['cop_self', 'cop_state', 'cop_connect_user', 'backuo2']
    list_display_links = None

    show_detail_fields = ('cop_self', )
    show_bookmarks = False

    def queryset(self):
        qs = SysManagerCopInfo.objects.all()
        return qs


xadmin.site.register(SystemPolicyCentralizedManagement, SystemPolicyCentralizedManagementAdmin)
xadmin.site.register(SecurityPolicyCentralizedManagement, SystemPolicyCentralizedManagementAdmin)
xadmin.site.register(AuditPolicyCentralizedManagement, SystemPolicyCentralizedManagementAdmin)

import xadmin
from ...api.models import SystemPolicyCentralizedManagement
from xadmin.views import ListAdminView
from .._1_xobj import SysManagerCopInfo, ConnectManagerUserInfo


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

    def cop_connect_user(self, instance):
        from ...xadmin.utils.self_utils import get_detaild_model
        return get_detaild_model(self, ConnectManagerUserInfo, instance.managers.all())

    cop_connect_user.short_description = "管理员用户集"
    cop_connect_user.allow_tags = True
    cop_connect_user.is_column = True

    list_display = ['cop_self', 'cop_state', 'cop_connect_user']
    list_display_links = None

    show_detail_fields = ('cop_self')
    show_bookmarks = False

    def queryset(self):

        qs = SysManagerCopInfo.objects.all()
        return qs


xadmin.site.register(SystemPolicyCentralizedManagement, SystemPolicyCentralizedManagementAdmin)


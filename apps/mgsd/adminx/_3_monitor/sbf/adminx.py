# coding:utf-8

from __future__ import absolute_import

import xadmin

from ....api.models import ConnectManagerUserInfo, ChangeAudit, SysManagerCopInfo
from ....api.monitor.models import ObjProcess, ProcessAuditLog
from ....api.none4cso.models import SystemRunningMonitor, AuditRunningMonitor, SecurityRunningMonitor


from xadmin.views import ListAdminView
from mgsd.api.chk.models import PolicyBaseTypes

from mgsd.xadmin.utils.self_utils import get_markd_table_details_show


class SystemRunningMonitorAdmin(ListAdminView):
    show_bookmarks = False
    list_display_links = None

    remove_permissions = ['add', 'change', 'delete']

    def get_process_name(self, instance):
        return get_markd_table_details_show(
            url=self.get_model_url(ObjProcess, 'changelist', ) + "{id}/detail/".format(
                id=instance.id), title=instance.process_name)
    get_process_name.short_description = "进程名称"

    def get_process(self, instance):
        return instance.process
    get_process.short_description = "部件进程唯一识别"

    def get_cop(self, instance):
        # return instance.report_time.strptime("%Y-%m-%d %H:%M:%S")
        return get_markd_table_details_show(
            url=self.get_model_url(SysManagerCopInfo, 'changelist', ) + "{id}/detail/".format(
                id=instance.cop.id), title=str(instance.cop) )
    get_cop.short_description = "所属部件"

    def the_last_monitor_time(self, instance):
        try:
            _the_last_monitor_obj = ProcessAuditLog.objects.filter(process=instance).order_by('-date_created')[0]
            return _the_last_monitor_obj.date_created.strftime('%m %d %H:%M:%S')
        except IndexError:
            return '-'

    the_last_monitor_time.short_description = "最近监控时间"
    the_last_monitor_time.allow_tags = True
    the_last_monitor_time.is_column = True

    def the_last_monitor_state(self, instance):
        try:
            _the_last_monitor_obj = ProcessAuditLog.objects.filter(process=instance).order_by('-date_created')[0]
            return _the_last_monitor_obj.get_process_stat_display()
        except IndexError:
            return '未受监控'

    the_last_monitor_state.short_description = "最近监控状态"
    the_last_monitor_state.allow_tags = True
    the_last_monitor_state.is_column = True

    list_display = ['get_process_name', 'get_cop', 'get_process', 'the_last_monitor_state', 'the_last_monitor_time']

    def queryset(self):
        qs = ObjProcess.objects.filter(process_type=PolicyBaseTypes[0][0])
        return qs


class SecurityRunningMonitorAdmin(SystemRunningMonitorAdmin):
    def queryset(self):
        qs = ObjProcess.objects.filter(process_type=PolicyBaseTypes[1][0])
        return qs


class AuditRunningMonitorAdmin(SystemRunningMonitorAdmin):
    def queryset(self):
        qs = ObjProcess.objects.filter(process_type=PolicyBaseTypes[2][0])
        return qs


xadmin.site.register(SystemRunningMonitor, SystemRunningMonitorAdmin)
xadmin.site.register(SecurityRunningMonitor, SecurityRunningMonitorAdmin)
xadmin.site.register(AuditRunningMonitor, AuditRunningMonitorAdmin)


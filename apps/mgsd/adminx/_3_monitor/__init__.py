import xadmin
from xadmin.layout import Fieldset
from xadmin.layout import Main, TabHolder, Tab, Fieldset, Row, Col, AppendedText, Side

from ...models import ObjProcess, ProcessAuditLog


class ObjProcessProcessAdmin(object):
    hidden_menu = True
    list_display = ['process_name', 'process_type', 'cop',
                    'process', 'user', 'date_created', 'the_last_monitor_time', 'the_last_monitor_state']
    list_editable = ['process_name', 'process_type', 'process']

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

    readonly_fields = ("date_created", "id")
    form_layout = (
            Main(
                  Tab(
                        "进程",
                        Fieldset(
                            "部件和生效", "process_name", "cop", "process", "user",
                            description="针对系统部件创建策略, 设置生效与否",
                        ),

                ),
            ),
            Side(
                Tab(
                    "指定部件进程监控类型",
                    Fieldset("process_type"),
                    # Inline(ActionInline)
                ),
           )
    )


class ProcessAuditAdmin(object):
    list_display = ('process_info', 'process_stat', 'date_created')
    hidden_menu = True

    def process_info(self, instance):
        return instance.process.cop.name + instance.process.process_name + " | " + instance.process.process + " | " + instance.process.get_process_type_display()
    process_info.short_description = "进程描述(部件|进程名|进程|类型)"
    process_info.allow_tags = True
    process_info.is_column = True


xadmin.site.register(ObjProcess, ObjProcessProcessAdmin)
xadmin.site.register(ProcessAuditLog, ProcessAuditAdmin)
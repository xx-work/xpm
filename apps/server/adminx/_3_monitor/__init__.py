import xadmin
from xadmin.layout import Fieldset
from xadmin.layout import Main, TabHolder, Tab, Fieldset, Row, Col, AppendedText, Side

from ...models import ObjProcess, ProcessAuditLog


class ObjProcessProcessAdmin(object):
    list_display = ['process_name', 'process_type', 'cop',
                    'process', 'user', 'date_created']
    list_editable = ['process_name', 'process_type', 'process']

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


xadmin.site.register(ObjProcess, ObjProcessProcessAdmin)
xadmin.site.register(ProcessAuditLog)
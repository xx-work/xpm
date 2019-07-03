import xadmin

from ...models import ChangeAudit


## 变更需要监控的对象有哪些，进行监控和处理跟进的审计。


class ChangeAuditAdmin(object):
    readonly_fields = ("opreate_username", )
    list_display = ('change_name', 'change_type', 'change_obj', 'change_desc', 'change_stat')
    list_filter = ['change_type', ]


xadmin.site.register(ChangeAudit, ChangeAuditAdmin)


from xadmin.models import Log
from xadmin.adminx import LogAdmin


class LogAdmin2(LogAdmin):
    list_per_page = 12
    hidden_menu = True


xadmin.site.unregister(Log)
xadmin.site.register(Log, LogAdmin2)

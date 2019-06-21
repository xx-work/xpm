import xadmin

from ...models import ChangeAudit


## 变更需要监控的对象有哪些，进行监控和处理跟进的审计。

class ChangeAuditAdmin(object):
    list_display = ('change_name', 'change_type', 'change_obj', 'change_desc', 'change_stat', '')


xadmin.site.register(ChangeAudit, ChangeAuditAdmin)
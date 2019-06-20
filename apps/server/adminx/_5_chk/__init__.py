import xadmin

from ...models import ChangeAudit


## 变更需要监控的对象有哪些，进行监控和处理跟进的审计。


xadmin.site.register(ChangeAudit)
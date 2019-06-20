import xadmin
from ...models import SystemPolicyCentralizedManagement, \
    SecurityPolicyCentralizedManagement, \
    AuditPolicyCentralizedManagement


xadmin.site.register(SystemPolicyCentralizedManagement)
xadmin.site.register(SecurityPolicyCentralizedManagement)
xadmin.site.register(AuditPolicyCentralizedManagement)



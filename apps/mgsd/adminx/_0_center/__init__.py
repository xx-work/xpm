import xadmin
from ...models import SystemPolicyCentralizedManagement, \
    SecurityPolicyCentralizedManagement, \
    AuditPolicyCentralizedManagement


from xadmin.views import ListAdminView

xadmin.site.register(SystemPolicyCentralizedManagement, ListAdminView)
xadmin.site.register(SecurityPolicyCentralizedManagement)
xadmin.site.register(AuditPolicyCentralizedManagement)



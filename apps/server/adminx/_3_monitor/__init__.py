import xadmin
from xadmin.layout import Fieldset

from ...models import ObjProcess, ProcessAuditLog


class ObjProcessProcessAdmin(object):
    list_display = ['process_name', 'process_type', 'cop',
                    'process', 'user','date_created']
    list_editable = ['process_name', 'process_type', 'process']



xadmin.site.register(ObjProcess, ObjProcessProcessAdmin)
xadmin.site.register(ProcessAuditLog)
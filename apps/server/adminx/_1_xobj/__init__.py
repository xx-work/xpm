import xadmin

from ...models import SysManagerCopInfo, ConnectManagerUserInfo, AuditLogObject


class SysManagerCopInfoAdmin(object):
    list_display = ['name', 'uniq_flag', 'pushed', 'up', 'ip', 'type', 'level', 'mac', 'os', 'mac_vendor']
    list_editable = ['uniq_flag', 'ip', 'name', 'pushed']

class ConnectManagerUserInfoAdmin(object):
    list_display = ['name', 'username', '_password', '_identity', '_protocol', 'is_active', 'date_created']
    list_editable = ['name', 'username', 'process', 'is_active']


xadmin.site.register(SysManagerCopInfo, SysManagerCopInfoAdmin)
xadmin.site.register(ConnectManagerUserInfo, ConnectManagerUserInfoAdmin)
xadmin.site.register(AuditLogObject)
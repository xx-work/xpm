import xadmin

from ...models import SysManagerCopInfo, ConnectManagerUserInfo


xadmin.site.register(SysManagerCopInfo)
xadmin.site.register(ConnectManagerUserInfo)
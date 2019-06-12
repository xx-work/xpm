import xadmin

from ...models import SnmpHostData, SnmpAgentCfgInfo, SystemObjProcess


xadmin.site.register(SnmpHostData)
xadmin.site.register(SnmpAgentCfgInfo)
xadmin.site.register(SystemObjProcess)
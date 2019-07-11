# coding:utf-8

# 三板斧之一 系统部件管理需要的models
from ..api.none4cso.models import *
# 上面的models可以永不注册。


from .xobj.models import SysManagerCopInfo, ConnectManagerUserInfo, AuditLogObject

from .policy.models import PolicyAction, PolicyBench, PolicyRule, PolicyActionHistory

from .monitor.models import ObjProcess, ProcessAuditLog

from .chk.models import ChangeAudit

from .solution.models import InfoSecEvent, AttackerActionDesc, EffectInfo, InfoGoin

from .backer.models import BackUpHistory


# 2019-7-11 注册新的策略APP
from .policy.policydetails.models import *



# coding:utf-8

# 加载核心部件管理的Model
from .api.xobj.models import SysManagerCopInfo, ConnectManagerUserInfo, AuditLogObject

from .api.policy.models import PolicyAction, PolicyBench, PolicyRule, PolicyActionHistory

from .api.monitor.models import ObjProcess, ProcessAuditLog

from .api.chk.models import ChangeAudit

from .api.solution.models import InfoSecEvent, AttackerActionDesc, EffectInfo, InfoGoin

from .api.backer.models import BackUpHistory


# 2019-7-11 注册新的策略APP
from .api.policy.policydetails.models import *


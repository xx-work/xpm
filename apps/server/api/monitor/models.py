from django.db import models
import uuid

STATES = (
    ("RUNING", "RUNING"),
    ("STOPED", "STOPED"),
    ("APPENDING", "APPENDING"),
)

from ..policy.models import PolicyBaseTypes


class ObjProcess(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    process_name = models.CharField(verbose_name="进程名称", max_length=255)
    process_stat = models.CharField(verbose_name="进程状态", max_length=55, choices=STATES)
    process_type = models.CharField(verbose_name="进程类型", max_length=100, choices=PolicyBaseTypes)
    date_create = models.DateTimeField(verbose_name="发现时间", auto_now_add=True)


from ..xobj.models import SysManagerCopInfo, ConnectManagerUserInfo

from django.contrib.auth.models import User
# 这里把平台用户省略，管理这个models 用 group

class SystemObjProcess(ObjProcess):
    cop = models.ForeignKey(SysManagerCopInfo, verbose_name="系统部件", related_name="sys_cop_process", on_delete=models.CASCADE)
    user = models.ManyToManyField(ConnectManagerUserInfo, verbose_name="系统部件用户", related_name="sys_user_process")
    # plat_user = models.ManyToManyField(User, verbose_name="平台用户", related_name="plat_user_process", on_delete=models.CASCADE)


## 监控内容；
## 系统进程; 监控系统部件的系统管理是否发生变化。配置等。



from django.db import models
import uuid


# 系统策略集中管理
class SystemPolicyCentralizedManagement(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)

    class Meta:
        verbose_name = "系统策略集中管理"

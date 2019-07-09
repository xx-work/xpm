from django.db import models
import uuid


# 策略集中管理
class SystemPolicyCentralizedManagement(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)

    class Meta:
        verbose_name = "系统策略集中管理"


class SecurityPolicyCentralizedManagement(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)

    class Meta:
        verbose_name = "安全策略集中管理"


class AuditPolicyCentralizedManagement(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)

    class Meta:
        verbose_name = "审计策略集中管理"


# 策略规则设置
class SystemPolicyRule(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)

    class Meta:
        verbose_name = "系统管理策略"


class SecurityPolicyRule(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)

    class Meta:
        verbose_name = "安全管理策略"


class AuditPolicyRule(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)

    class Meta:
        verbose_name = "审计管理策略"


# 运行监控
class SystemRunningMonitor(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)

    class Meta:
        verbose_name = "系统部件运行监控"


class SecurityRunningMonitor(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)

    class Meta:
        verbose_name = "安全机制变更管理"


class AuditRunningMonitor(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)

    class Meta:
        verbose_name = "审计机制变更管理"


# 变更管理
class SystemChangeAudit(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)

    class Meta:
        verbose_name = "系统变更管理"


class SecurityChangeAudit(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)

    class Meta:
        verbose_name = "安全变更管理"


class AuditChangeAudit(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)

    class Meta:
        verbose_name = "审计变更管理"


# 事件响应处置
class SystemEventResponseSolve(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)

    class Meta:
        verbose_name = "系统事件响应处置"


class SecurityEventResponseSolve(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)

    class Meta:
        verbose_name = "安全事件响应处置"


class AuditEventResponseSolve(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)

    class Meta:
        verbose_name = "审计事件响应处置"
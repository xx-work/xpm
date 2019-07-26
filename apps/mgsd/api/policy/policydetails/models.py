from django.db import models
import uuid

PushedType = (
    ("username", "用户名强度"),
    ("password", "密码强度"),
)


class PasswordQuerySet(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    type = models.CharField(max_length=55, verbose_name="应用强度类型", default='password')
    name = models.CharField(max_length=55, verbose_name="密码名称", default='基本强度密码')
    desc = models.CharField(max_length=55, verbose_name="密码描述", default='字母数字在8-16范围内')
    rgx = models.CharField(max_length=255, verbose_name="密码正则", default='[\d\w_]{8,16}')
    active = models.BooleanField(default=True, verbose_name='是否生效')
    date_created = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    def __str__(self):
        return str(self.name)

    class Meta:
        db_table = "password_selected"
        verbose_name = u"密码安全管理"


LogYUChoices = (
    ('Clear', '清理日志'),
    ('Alert', '仅告警和通知管理员'),
    ('C&A', '清理日志并通知管理员'),
)


class LogMgQuerySet(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)

    log_expire = models.IntegerField(verbose_name='日志有效期', default=200)
    log_max_free = models.FloatField(verbose_name='日志最小空闲值', default=200.5)
    log_max_used = models.FloatField(verbose_name='日志最大使用值', default=700.5)

    solve = models.CharField(choices=LogYUChoices, max_length=33, default='C&A', verbose_name='设置日志到达阈值的处理措施')

    auto_backup = models.BooleanField(default=False, verbose_name='是否自动备份')
    default_backup_crontab = models.CharField(max_length=55, verbose_name="备份时间描述", default='每周一 1:0')
    default_backup_path = models.CharField(max_length=55, verbose_name="默认本地备份位置", default='/srv/data/log')
    date_created = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    def __str__(self):
        return str(self.id)

    @staticmethod
    def get_latest_config():
        return LogMgQuerySet.objects.all().order_by('-date_created')[0]

    class Meta:
        db_table = "log_mg"
        verbose_name = u"日志管理"


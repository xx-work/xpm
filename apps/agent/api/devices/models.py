from django.db import models
import uuid

METHODS = (
    ('get', 'GET'),
    ('post', 'POST'),
    ('put', 'PUT'),
    ('delete', 'DELETE'),
    ('option', 'OPTION'),
)

from mgsd.api.xobj.models import SysManagerCopInfo


class AgentApi(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    prefix = models.CharField(verbose_name="URL前缀", max_length=200, default='http://localhost:8000')
    url = models.CharField(verbose_name="URL", max_length=200, default='/')
    data = models.CharField(verbose_name="payload", max_length=255, default='')
    method = models.CharField(verbose_name="进程类型", max_length=100, choices=METHODS)
    auth = models.BooleanField(verbose_name='需要认证', default=True)
    params = models.CharField(verbose_name="请求参数", max_length=255, default='')
    name = models.CharField(verbose_name="API名称", max_length=255, default='')
    desc = models.CharField(verbose_name="API描述", max_length=255, default='')
    _type = models.CharField(verbose_name="API类型", max_length=255, default='')
    response_eg = models.CharField(verbose_name="响应举例", max_length=255, default='')
    error_eg = models.CharField(verbose_name="错误响应举例", max_length=255, default='')
    example = models.CharField(verbose_name="使用举例", max_length=255, default='')
    agent = models.ForeignKey(SysManagerCopInfo, verbose_name='部件', related_name='cop_api', on_delete=models.CASCADE)

    # date_created = models.DateTimeField(auto_now_add=True, verbose_name="API录入时间")
    date_updated = models.DateTimeField(auto_now=True, verbose_name="API修改时间")

    def __str__(self):
        return str(self.method) + " " + str(self.prefix) + str(self.url)

    class Meta:
        db_table = "agent_api"
        verbose_name = "系统部件的API"
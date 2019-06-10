from django.db import models
import uuid

STATES = (
    ("RUNING", "RUNING"),
    ("STOPED", "STOPED"),
    ("APPENDING", "APPENDING"),
)


class ObjProcess(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    process_name = models.CharField(verbose_name="进程名称", max_length=255)
    process_stat = models.CharField(verbose_name="进程名称", max_length=55, choices=STATES)
    date_create = models.DateTimeField(verbose_name="发现时间", auto_now_add=True)



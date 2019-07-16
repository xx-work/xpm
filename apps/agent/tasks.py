# coding: utf-8
from __future__ import absolute_import, unicode_literals

import subprocess
import sys
import os
import django
from celery import shared_task
from ops.celery.decorator import register_as_period_task


def django_setup():

    django_module_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    sys.path.append(django_module_path)
    os.chdir(django_module_path)
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "website.settings")
    django.setup()


django_setup()


@shared_task
def push_cmd(cmd):
    p = subprocess.Popen(cmd, shell=True)
    import time
    time.sleep(1)
    os.waitpid(p.pid, os.W_OK)
    return {
        "stat": True,
        "cmd": cmd,
        "reason": "远程执行命令执行成功！"
    }

@shared_task
@register_as_period_task(interval=60 * 2)
def sysdatas2db():
    """
    将SNMP获取的系统信息全部存储到数据库
    :return:
    """
    from agent.minitord.snmpd.snmp import collect_datas
    collect_datas()
    return {
        "stat": True,
        "reason": "SNMP数据存储完成"
    }


@shared_task
def miguan_alerts_tasks(_all_lists, data):
    """
    导入蜜罐的数据到这里面来
    :param _all_lists:
    :param data:
    :return:
    """
    from agent.abstracts.alerts.api_view import alerts_input_tasks
    res = alerts_input_tasks(_all_lists, data)

    return {
        "stat": True,
        "reason": res
    }

# coding:utf-8
from __future__ import absolute_import, unicode_literals

import subprocess
import sys
import os
import django
from celery import shared_task, chain, chord
from services.celery.decorator import register_as_period_task

def django_setup():
    DjangoModulePath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    sys.path.append(DjangoModulePath)
    os.chdir(DjangoModulePath)
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "website.settings")
    django.setup()


__NMAP_SCAN_XML_PATH = "__NMAP_SCAN_XML_PATH"

@shared_task
def nmap_scan(targets="192.168.2.73 192.168.2.41"):
    django.setup()

    from server.api.system.mudules.monitor.nmap_tool.nmap_conf import (
        NmapDataDir, NmapScanDefaultBin, NmapScanDefaultArgs, Nmap_xml_result_path
    )
    cmds = [
        NmapScanDefaultBin
    ]
    cmds.extend(NmapScanDefaultArgs.split(" "))
    cmds.extend([targets, ])
    cmds.extend(["-oX", Nmap_xml_result_path])

    # from django.core.cache import cache
    # cache.set(__NMAP_SCAN_XML_PATH, Nmap_xml_result_path)
    try:
        p = subprocess.Popen(cmds)
        import time
        time.sleep(1)
        os.waitpid(p.pid, os.W_OK)
    except:
        print("\n>>>>>>>>>>>>>>>>>>>Nmap--ERROR----\n")
    return Nmap_xml_result_path


@shared_task
def send_email(object="actanble@163.com"):
    django_setup()
    from django.core.mail import send_mail
    send_mail('CSO_ERROR: Nmap-Extract Error.', 'Here is the message.', 'actanble@163.com',
              ['2970090120@qq.com', object], fail_silently=False)
    return "Send Success!"


@shared_task
def nmap_result_import(xml_path):
    django_setup()

    from server.api.system.mudules.monitor.nmap_tool.get_nmap_datas import get_needs_datas_from_xmlpath
    try:
        # from django.core.cache import cache
        # _path = cache.get(__NMAP_SCAN_XML_PATH)
        get_needs_datas_from_xmlpath(xml_path)
        return "Nmap Scan Result Extract Sucess!"
    except Exception as e:
        print(e)
        import logging
        alert = "[!]Nmap Scan Result Extract Faild!"
        logging.error(alert)
        send_email.delay()
        return alert


@shared_task
@register_as_period_task(interval=3600*3)
def chain_tasks(targets="192.168.2.73 192.168.2.41 192.168.2.99"):
    # chord(header=[ nmap_scan.s(), ], body=nmap_result_import.s() )()
    chain(nmap_scan.s(targets), nmap_result_import.s())()
    return "Task End"


@shared_task
def post_cmd(cmd):
    try:
        p = subprocess.Popen(cmd, shell=True)
    except Exception as e:
        print(e)


@register_as_period_task(interval=60 * 2)
@shared_task
def push_monitor_datas():
    django_setup()

    from server.api.system.mudules.monitor.snmp.collect import collect_datas
    collect_datas()
    return None
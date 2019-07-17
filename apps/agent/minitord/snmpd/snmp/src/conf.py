# -*- coding: utf-8 -*-
# @Time    : 2019/3/15 10:58
# @Author  : Zcs
# @File    : config.py
config_template = {
    'MYSQL': {'CHARSET': 'utf8', 'DB': 'cso', 'HOST': '192.168.2.101', 'PASSWD': 'myadmin@816', 'PORT': 3306,'USER': 'admin007'},
    'SNMP_OID': {
        'cpu_percent': {'oid': '1.3.6.1.4.1.2021.11.9.0', 'req_method': 'get'},
        'disk_percent': {'oid': '1.3.6.1.4.1.2021.9.1.9', 'req_method': 'walk'},
        'disk_total': {'oid': '1.3.6.1.4.1.2021.9.1.6', 'req_method': 'walk'},
        'if_mac': {'oid': '1.3.6.1.2.1.2.2.1.6', 'req_method': 'walk'},
        'if_name': {'oid': '1.3.6.1.2.1.2.2.1.2', 'req_method': 'walk'},
        'if_recv_flow': {'oid': '1.3.6.1.2.1.2.2.1.10', 'req_method': 'walk'},
        'if_send_flow': {'oid': '1.3.6.1.2.1.2.2.1.16', 'req_method': 'walk'},
        'if_status': {'oid': '1.3.6.1.2.1.2.2.1.8', 'req_method': 'walk'},
        'real_mem_total': {'oid': '1.3.6.1.4.1.2021.4.5.0', 'req_method': 'get'},
        'real_mem_used': {'oid': '1.3.6.1.4.1.2021.4.6.0', 'req_method': 'get'},
        'swap_mem_ava': {'oid': '1.3.6.1.4.1.2021.4.4.0', 'req_method': 'get'},
        'swap_mem_total': {'oid': '1.3.6.1.4.1.2021.4.3.0', 'req_method': 'get'},
        'sys_desc': {'oid': '1.3.6.1.2.1.1.1.0', 'req_method': 'get'},
        'sys_ip': {'oid': 'IP-MIB::ipAdEntAddr', 'req_method': 'walk'},
        'sys_mask': {'oid': 'IP-MIB::ipAdEntNetMask', 'req_method': 'walk'},
        'sys_open_port': {'oid': '1.3.6.1.2.1.6.13.1.1', 'req_method': 'walk'},
        'sys_run_process': {'oid': '1.3.6.1.2.1.25.4.2.1.2', 'req_method': 'walk'},
        'sys_software': {'oid': '1.3.6.1.2.1.25.6.3.1.2', 'req_method': 'walk'},
        'sys_up_time': {'oid': '1.3.6.1.2.1.1.3', 'req_method': 'walk'}
    },
    'ALARM_POLICY': {
        0: {'target_name': 'CPU使用率'},
        1: {'target_name': '内存使用率'},
        2: {'target_name': '硬盘使用率'},
    },
    'ALARM_ACTION': {
        0: ">",
        1: "<",
        2: "=",
    },
}

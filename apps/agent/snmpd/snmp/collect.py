from .src.dev import DevSnmpHandler
from .models import SnmpAgentCfgInfo, SnmpHostData


def get_datas_from_cfg(ip, port, community):

    snmp_handler = DevSnmpHandler(ip=ip, port=port, community=community)
    try:
        send_flow, recv_flow = snmp_handler.get_current_flow()
        cpu_percent, mem_percent, disk_percent = snmp_handler.get_percent_data()
        # up_time = snmp_handler.get_up_time()
        response = dict(
            send_flow=send_flow,
            recv_flow=recv_flow,
            cpu_percent=cpu_percent,
            mem_percent=mem_percent,
            disk_percent=disk_percent,
            # up_time=int(up_time),
        )
        return response
    except Exception as e:
        import logging
        logging.error("【{}】 ".format(ip) + e + "Error: SNMP_OID")
        return None


def collect_datas():
    # SnmpHostData.objects.all().delete()
    for x in SnmpAgentCfgInfo.objects.filter(collected=True):
        _datas = get_datas_from_cfg(ip=x.cop.ip, port=x.snmp_port, community=x.snmp_community)
        if _datas:
            SnmpHostData.objects.create(cop=x.cop, **_datas)
    import logging
    logging.warning("统计SNMP收集的数据完成")



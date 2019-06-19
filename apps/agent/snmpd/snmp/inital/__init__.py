
prepared_data = [
    {"ip":"192.168.2.41", "port": 161, "community": "sysinfo" },
    {"ip":"192.168.2.73", "port": 161, "community": "sysinfo" },
    {"ip":"192.168.2.17", "port": 161, "community": "sysinfo" },

]


def inital_data():
    from ..models import SnmpHostData, SnmpAgentCfgInfo, SysManagerCopInfo
    for x in prepared_data:
        _ip = x["ip"]
        if _ip not in [y.ip for y in SysManagerCopInfo.objects.all()]:
            _cop = SysManagerCopInfo.objects.create(uniq_flag=_ip, ip=_ip, name="Snmp-Add")
        else:
            # 注意这里不要把IP搞成一样的
            _cop = SysManagerCopInfo.objects.objects.filter(ip=_ip)[0]

        SnmpAgentCfgInfo.objects.create(
            cop=_cop,
            snmp_port=x["port"],
            snmp_community = x["community"],
        )
    print("创建完成。")





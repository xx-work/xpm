from libnmap.parser import NmapParser
import uuid

from xsqlmb.src.ltool.utils.dt_tool import get_pydt_based_logdt, get_pydt2_based_nmap
from cso.mudules.monitor.cop_info import create_cop_default_user

from cso.mudules.monitor.models import HostService
from cso.models import SysManagerCopInfo, ConnectManagerUserInfo

path = "F:\\workspace\\CSO\\apps\\cso\\datas\\nmap_results\\sV.xml"


def cop_in_plat(_host):
    _ip = _host.id
    _mac = _host.mac
    _vendor = _host.vendor
    _filters = SysManagerCopInfo.objects.filter(mac=_mac)
    if len(_filters) > 0:
        _cop = _filters[0]
    else:
        _cop = SysManagerCopInfo(
            uniq_flag="CommonHost" + str(uuid.uuid4()),
            name=_ip,
            ip=_ip,
            type="自发现设备",
            os="Centos-7.4",
            mac=_mac,
            mac_vendor=_vendor,
            up=True,
        )
        _cop.save()
        _cop.managers.add(create_cop_default_user())
    return dict(
        _cop=_cop,
        _ip=_host.id,
        _mac = _host.mac,
        _vendor = _host.vendor,
    )


def get_needs_datas_from_xmlpath(xml_path=path, incomplete=False, debug=True):
    nmap_report = NmapParser.parse_fromfile(xml_path, incomplete=incomplete)
    # print(nmap_report._scaninfo)
    # print(nmap_report._runstats)
    # print(nmap_report._nmaprun)
    _time = get_pydt2_based_nmap(nmap_report._runstats["finished"]["timestr"])
    # print(_time)
    _services_list = []

    # 2019-5-28 修改; 服务状态监控, 为时间监控
    judge_hosts_services_stat(nmap_report)

    # SysManagerCopInfo.objects.all().delete()
    # HostService.objects.all().delete()
    for _host in nmap_report.hosts:
        _cop_info = cop_in_plat(_host)
        _ip = _cop_info["_ip"]
        _cop = _cop_info["_cop"]

        for _service in _host.services:
            service = _service.get_dict()
            del service["id"]
            # print(service)
            _services_list.append( HostService(**service, descover_time=_time, belongCop=_cop), )

    HostService.objects.bulk_create(_services_list)



def judge_hosts_services_stat(nmap_report):
    _services_list = []
    survived_hosts = [_host.id for _host in nmap_report.hosts ]
    for host in SysManagerCopInfo.objects.all():
        _up = host.up ## 之前的状态
        if host.ip in survived_hosts:
            if _up == True:
                continue
            host.up = True
        else:
            if _up == False:
                continue
            host.up = False
        host.save()

    for service in HostService.objects.all():
        _up = service.running
        if service.belongCop.ip in survived_hosts:
            if _up == True:
                continue
            service.running = True
        else:
            if _up == False:
                continue
            service.running = False
        service.save()



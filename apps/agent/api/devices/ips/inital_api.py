from .fips.api import ApiINfo, IPS_API

from mgsd.api.xobj.models import SysManagerCopInfo
ips_cop = SysManagerCopInfo.objects.get(uniq_flag='ips_cya_0726')

from ..models import AgentApi


def push_ips_apis():
    for x in IPS_API:
        data = AgentApi(**x.todict())
        data.agent = ips_cop
        data.save()

        print(x)



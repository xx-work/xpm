import xadmin

from ..models import SnmpHostData, SnmpAgentCfgInfo


class SnmpAgentCfgInfoAdmin(object):
    list_display = ['cop', 'snmp_port', 'snmp_community', 'collected']
    list_editable = ['snmp_port', 'snmp_community', 'collected']

    # form_layout = (
    #     Fieldset("名称", 'name', 'summary'),
    #     Fieldset(None, 'user', 'desc', 'id', **{"style": "display:None"}),
    # )


class SnmpHostDataAdmin(object):
    list_display = ['cop', 'send_flow', 'recv_flow', 'cpu_percent', 'mem_percent', 'disk_percent', 'up_time', 'date_created']


xadmin.site.register(SnmpHostData, SnmpHostDataAdmin)
xadmin.site.register(SnmpAgentCfgInfo, SnmpAgentCfgInfoAdmin)


from django_celery_beat.models import PeriodicTask, CrontabSchedule, IntervalSchedule
xadmin.sites.register(PeriodicTask)
xadmin.sites.register(CrontabSchedule)
xadmin.sites.register(IntervalSchedule)


import xadmin

from ..models import SnmpHostData, SnmpAgentCfgInfo


class SnmpAgentCfgInfoAdmin(object):
    list_display = ['cop', 'snmp_port', 'snmp_community', 'collected']
    list_editable = ['snmp_port', 'snmp_community', 'collected']

    # form_layout = (
    #     Fieldset("名称", 'name', 'summary'),
    #     Fieldset(None, 'user', 'desc', 'id', **{"style": "display:None"}),
    # )
    hidden_menu = True


class SnmpHostDataAdmin(object):
    isExecute = True

    def send_flow_m(self, instance):
        return round(float(instance.send_flow / 1024 / 1024), 3)
    send_flow_m.short_description = "发送字节数(M)"
    send_flow_m.allow_tags = True
    send_flow_m.is_column = True

    def recv_flow_m(self, instance):
        return round(float(instance.recv_flow / 1024 / 1024), 3)
    recv_flow_m.short_description = "接受字节数(M)"
    recv_flow_m.allow_tags = True
    recv_flow_m.is_column = True

    list_per_page = 20
    list_display = ['cop', 'send_flow_m', 'recv_flow_m', 'cpu_percent', 'mem_percent', 'disk_percent', 'up_time', 'date_created']
    list_filter = ['cop', 'date_created', ]

    def date_showd(self, instance):
        return instance.date_created.strftime('%m-%d %H:%M')
    date_showd.short_description = "时间"
    date_showd.allow_tags = True
    date_showd.is_column = True

    data_charts = {
        "系统资源占用统计": {'title': u"CPU/内存/硬盘占用统计", "x-field": "date_showd",
                   "y-field": ('cpu_percent', 'mem_percent', 'disk_percent'),
                   "option": {
                       "series": {"bars": {"align": "center", "barWidth": 0.2, 'show': False}},
                "xaxis": {"mode": "categories"},
            },
        },
        "网口流量统计": {'title': u"进出流量统计", "x-field": "date_showd",
                    "y-field": ('send_flow_m', 'recv_flow_m'),
                    "option": {
                        "series": {"bars": {"align": "center", "barWidth": 0.2, 'show': False}},
                  "xaxis": {"mode": "categories"},
          },
        },
    }

    hidden_menu = True


xadmin.site.register(SnmpHostData, SnmpHostDataAdmin)
xadmin.site.register(SnmpAgentCfgInfo, SnmpAgentCfgInfoAdmin)


from django_celery_beat.models import PeriodicTask, CrontabSchedule, IntervalSchedule
xadmin.sites.register(PeriodicTask)
xadmin.sites.register(CrontabSchedule)
xadmin.sites.register(IntervalSchedule)





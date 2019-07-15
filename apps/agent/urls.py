from django.conf.urls import url

urlpatterns = []

from agent.minitord.snmpd.views import collect_data
urlpatterns += [
    url('collect_data_cso_snmp_v2', collect_data),     ## 生成令牌
]


from agent.abstracts.alerts.api_view import push_pot_data_to_cso_alerts
urlpatterns += [
    url('pushd_pot_data', push_pot_data_to_cso_alerts, name='push_pot_data_to_cso_alerts'),     ## 生成令牌
]

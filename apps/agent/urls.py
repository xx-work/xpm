from django.conf.urls import url

urlpatterns = []

from agent.minitord.snmpd.views import collect_data
urlpatterns += [
    url('collect_data_cso_snmp_v2', collect_data),     ## 生成令牌
]


from ..modesl import PolicyBaseTypes
policy_types = [x[0] for x in PolicyBaseTypes]

# 1系统管理策略
# 2安全机制策略
# 3审计机制策略


get_policy_rule_obj = lambda type_id, key, value, name, desc : dict(
    type=policy_types[type_id],
    key=key,
    name=name,
    desc=desc,
)


POLICY_BASE_DEFAULTS = [
    [1, "host_survice_monitor_period", 60, "主机存活探测周期", "判断监控的主机是否是开机状态"],
    [1, "service_survice_monitor_period", 60, "主要服务探测周期", "判断被监控的服务是否是可以提供服务的状态"],
    [1, "hosts_monitor_period", 60, "主要服务探测周期", "判断被监控的服务是否是可以提供服务的状态"],

]
"""
- 主机存活探测周期
- 主机服务探测周期
- 主机信息收集周期
"""



POLICY_RULES_DEFAULTS = [


]
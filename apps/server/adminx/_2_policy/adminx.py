import xadmin

from ...models import PolicyBench, PolicyAction, PolicyRule, PolicyActionHistory


class PolicyBenchAdmin(object):
    list_display = ("name", "desc", "type", "date_created")


class PolicyActionAdmin(object):
    list_display = ("action_name", "cop_user", "belong_cop", "_connect_agent", '_connect_kwargs')


class PolicyRuleAdmin(object):
    list_display = ['belong_cop', 'policy_bench', 'plat_username', 'active', 'policy_action']


xadmin.site.register(PolicyBench, PolicyBenchAdmin)
xadmin.site.register(PolicyAction, PolicyActionAdmin)
xadmin.site.register(PolicyRule, PolicyRuleAdmin)
xadmin.site.register(PolicyActionHistory)
# coding:utf-8

import xadmin
from ....api.models import SystemCopPolicyRule

from ....api.policy.models import PolicyBaseTypes, PolicyRule, PolicyAction, PolicyBench

from xadmin.views import ListAdminView

from django.utils.safestring import mark_safe


class SystemCopPolicyRuleAdmin(ListAdminView):
    show_bookmarks = False
    list_display_links = None

    def get_rule_cop(self, instance):
        return instance.belong_cop

    def get_rule_bench(self, instance):
        return instance.policy_bench

    def get_rule_user(self, instance):
        return instance.plat_username

    def get_rule_add_time(self, instance):
        return instance.add_time

    list_display = ('get_rule_cop', 'get_rule_bench', 'get_rule_user', 'get_rule_add_time')

    def queryset(self):
        qs = PolicyRule.objects.filter(policy_bench__type=PolicyBaseTypes[0][0])
        return qs


xadmin.site.register(SystemCopPolicyRule, SystemCopPolicyRuleAdmin)

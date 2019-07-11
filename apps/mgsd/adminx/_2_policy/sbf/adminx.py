# coding:utf-8

from __future__ import absolute_import

import xadmin
from ....api.models import SecurityPolicyRule, SystemPolicyRule, AuditPolicyRule
from ....api.models import ConnectManagerUserInfo, SysManagerCopInfo

from ....api.policy.models import PolicyBaseTypes, PolicyRule, PolicyAction, PolicyBench

from xadmin.views import ListAdminView

from mgsd.xadmin.utils.self_utils import get_markd_table_details_show


class SystemCopPolicyRuleAdmin(ListAdminView):
    show_bookmarks = False
    list_display_links = None

    remove_permissions = ['add', 'change', 'delete']

    def get_rule_cop(self, instance):
        return get_markd_table_details_show(
            url=self.get_model_url(SysManagerCopInfo, 'changelist', ) + "{id}/detail/".format(
                id=instance.belong_cop.id), title=instance.belong_cop.name)

    get_rule_cop.short_description = "管理的系统部件"

    def get_rule_bench(self, instance):
        return get_markd_table_details_show(
            url=self.get_model_url(PolicyBench, 'changelist', ) + "{id}/detail/".format(
                id=instance.policy_bench.id), title=instance.policy_bench.name)
    get_rule_bench.short_description = "关联的规则基准"

    def get_rule_user(self, instance):
        plat_user = ConnectManagerUserInfo.objects.get(username=instance.plat_username)
        return get_markd_table_details_show(
            url=self.get_model_url(ConnectManagerUserInfo, 'changelist', ) + "{id}/detail/".format(
                id=plat_user.id), title=plat_user.name)
    get_rule_user.short_description = "策略用户"

    def get_rule_add_time(self, instance):
        return instance.add_time
    get_rule_add_time.short_description = "策略添加时间"

    list_display = ('get_rule_cop', 'get_rule_bench', 'get_rule_user', 'get_rule_add_time')

    def queryset(self):
        qs = PolicyRule.objects.filter(policy_bench__type=PolicyBaseTypes[0][0])
        return qs


from django.shortcuts import reverse


class SecurityPolicyRuleAdmin(SystemCopPolicyRuleAdmin):
    def queryset(self):
        return PolicyRule.objects.filter(policy_bench__type=PolicyBaseTypes[1][0])

    def get_context(self):
        context = super(SecurityPolicyRuleAdmin, self).get_context()
        title = "安全管理策略总览"  # 定义面包屑变量

        context["breadcrumbs"].append({'url': reverse('get_latest_password_policy'), 'title': '密码策略管理'})
        context["breadcrumbs"].append({'url': '/admin/group_perm_view?group_id=1', 'title': '安全权限视图查看'})
        context["breadcrumbs"].append({'title': title})  # 把面包屑变量添加到context里面
        return context


class AuditPolicyRuleAdmin(SystemCopPolicyRuleAdmin):
    def queryset(self):
        return PolicyRule.objects.filter(policy_bench__type=PolicyBaseTypes[2][0])

    def get_context(self):
        context = super(AuditPolicyRuleAdmin, self).get_context()
        title = "审计管理策略总览"  # 定义面包屑变量
        context["breadcrumbs"].append(
            {'url': reverse('get_latest_log_policy'), 'title': '日志备份策略管理'})  # 把面包屑变量添加到context里面

        context["breadcrumbs"].append({'title': title})  # 把面包屑变量添加到context里面
        return context


xadmin.site.register(SystemPolicyRule, SystemCopPolicyRuleAdmin)
xadmin.site.register(SecurityPolicyRule, SecurityPolicyRuleAdmin)
xadmin.site.register(AuditPolicyRule, AuditPolicyRuleAdmin)
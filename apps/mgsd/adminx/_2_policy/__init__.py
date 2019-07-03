import xadmin
from xadmin.filters import MultiSelectFieldListFilter
from xadmin.layout import Main, TabHolder, Tab, Fieldset, Row, Col, AppendedText, Side
from xadmin.plugins.inline import Inline

from ...models import PolicyBench, PolicyAction, PolicyRule, PolicyActionHistory


class BenchInline(object):
    model = PolicyBench
    # extra = 1
    # style = "accordion"


class ActionInline(object):
    model = PolicyAction
    # extra = 1
    # style = "accordion"


class PolicyBenchAdmin(object):
    list_filter = ['type', ]
    list_display = ("name", "desc", "type", "date_created")
    hidden_menu = True


class PolicyActionAdmin(object):
    hidden_menu = True
    def pushed(self, instance):
        return """<a href="/sys/pushed?sid={}">策略下发</a>""".format( str(instance.id) )
    pushed.short_description = "策略下发"
    pushed.allow_tags = True
    pushed.is_column = True

    list_display = ("action_name", "cop_user", "belong_cop", "_connect_agent", '_connect_kwargs', 'pushed')
    # list_quick_filter = ["service_type", {"field": "idc__name", "limit": 10}]


class PolicyRuleAdmin(object):
    hidden_menu = True
    def policy_type(self, instance):
        return instance.policy_bench.get_type_display()
    policy_type.short_description = "策略类型"
    policy_type.allow_tags = True
    policy_type.is_column = True

    list_display = ['belong_cop', 'policy_bench', 'policy_type', 'policy_action', 'plat_username', 'active', ]

    style_fields = {"system": "radio-inline"}
    search_fields = ["action_name", ]

    list_filter = [
        "policy_bench__type", "plat_username", "active",
        (
            "belong_cop",
            MultiSelectFieldListFilter,
        ),
    ]

    save_as = True
    # aggregate_fields = {"add_time": "min"}
    # grid_layouts = ("table", "thumbnails")

    def save_models(self):
        instance = self.new_obj
        request = self.request
        if not instance.plat_username:
            instance.plat_username = request.user.username
        instance.save()

    readonly_fields = ("plat_username", "id")
    form_layout = (
        Main(
            Tab(
                "策略规则对象指定",
                Fieldset(
                    "部件和生效", "belong_cop", "active", description="针对系统部件创建策略, 设置生效与否",
                    ),
                    Inline(BenchInline),
                ),
        ),
        Side(
            Tab(
                "策略基准和指定策略下发",
                # Fieldset("policy_action"),
                Inline(ActionInline)
            ),

        )
    )


class PolicyHistoryAdmin(object):
    hidden_menu = True

    def action_name(self, instance):
        return instance.policyaction.action_name
    action_name.short_description = "操作"
    action_name.allow_tags = True
    action_name.is_column = True

    list_display = ('action_name', 'filter_type', 'response', 'add_time')


xadmin.site.register(PolicyBench, PolicyBenchAdmin)
xadmin.site.register(PolicyAction, PolicyActionAdmin)
xadmin.site.register(PolicyRule, PolicyRuleAdmin)
xadmin.site.register(PolicyActionHistory, PolicyHistoryAdmin)
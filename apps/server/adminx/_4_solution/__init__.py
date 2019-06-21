import xadmin
from xadmin.layout import Main, TabHolder, Tab, Fieldset, Row, Col, AppendedText, Side
from ...models import InfoSecEvent, InfoGoin, EffectInfo, AttackerActionDesc


class InfoSecEventAdmin(object):
    list_display = ['infosysname', 'info_type', 'describtion',
                    'info_level', 'descover_time', 'happend_time', 'reporter', 'report_time']
    readonly_fields = ("reporter", "id")

    # wizard_form_list = [
    #     ('事件内容', {'fields': ['infosysname', 'info_type', 'describtion', 'info_level']}),
    #     ('发生和发现', {'fields': ['descover_time', 'happend_time', 'reporter']}),
    #     ('事件性质', {'fields': ['negative_impacts', "attacker_descs"]}),
    #     ('影响范围', {'fields': ['impact_cops']}),
    #     ('计划措施', {'fields': ['plan_action']}),
    # ]

    form_layout = (
        Main(
                Tab(
                    "事件内容",
                    Fieldset(
                        "手动增加事件", 'infosysname', 'info_type', 'describtion', 'info_level',
                        description="事件内容",
                    ),
                    Fieldset(
                        "发生和发现", 'descover_time', 'happend_time', 'reporter',
                        description="发生和发现",
                    ),
                    Fieldset(
                        "事件性质", 'negative_impacts', "attacker_descs",
                        description="事件性质",
                    ),
                    Fieldset(
                        "影响范围", 'impact_cops',
                        description="影响范围",
                    ),
                ),
        ),
        Side(
            Tab(
                "计划措施",
                # Fieldset("policy_action"),
                Fieldset(
                    "计划措施", 'plan_action',
                    description="计划措施",
                ),
            ),

        )
    )

    def save_models(self):
        instance = self.new_obj
        request = self.request
        if not instance.reporter:
            instance.reporter = request.user.username
        instance.save()


class InfoGoingAdmin(object):
    list_display = ['info', 'go_user',  'state', 'had_action', 'state', 'go_time']
    readonly_fields = ["id", 'go_user']

    def save_models(self):
        instance = self.new_obj
        request = self.request
        if not instance.go_user:
            instance.go_user = request.user.username
        instance.save()


xadmin.site.register(InfoSecEvent, InfoSecEventAdmin)

xadmin.site.register(EffectInfo)
xadmin.site.register(AttackerActionDesc)
xadmin.site.register(InfoGoin, InfoGoingAdmin)

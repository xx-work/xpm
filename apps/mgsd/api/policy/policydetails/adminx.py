import xadmin
from .models import PasswordQuerySet, LogMgQuerySet
from xadmin.layout import Main, TabHolder, Tab, Fieldset, Row, Col, AppendedText, Side

from xadmin.views import ModelFormAdminView
from mgsd.api.models import SecurityPolicyRule, AuditPolicyRule


class PasswordQuerySetAdmin(object):
    list_display_links = None
    # remove_permissions = ['add', 'change', 'delete']
    hidden_menu = True
    list_display = ['type', 'name', 'desc', 'rgx', 'active']
    readonly_fields = ['id', 'type']
    form_layout = (
        Main(
            Tab(
                "设置密码强度",
                Fieldset(
                    "密码强度",
                    Row('name', 'rgx'),
                    Row('desc', ),
                    # Row('active', ),
                    description="设置密码强度, 这则表达式和设置, 如果没有将会使用默认的。",
                ),

            ),

        ),
        Side(
            Tab(
                "状态",
                Fieldset("是否生效", 'active', ),
            ),
            Tab(
                "",
                Fieldset("", 'type', ),
            ),
        )
    )

    def queryset(self):
        qs = PasswordQuerySet.objects.all()
        if len(qs) < 1:
            _default = PasswordQuerySet()
            _default.save()
        return qs

    def get_context(self):
        context = super(PasswordQuerySetAdmin, self).get_context()
        title = "安全管理策略总览"  # 定义面包屑变量
        context["breadcrumbs"].append({'url': self.get_model_url(SecurityPolicyRule, 'changelist'), 'title': '审计策略管理'})
        context["breadcrumbs"].append({'title': title})  # 把面包屑变量添加到context里面
        return context

class LogMgQuerySetAdmin(object):
    list_display_links = None
    # remove_permissions = ['add', 'change', 'delete']
    hidden_menu = True
    list_display = ['auto_backup', 'log_expire', 'default_backup_path',
                    'log_expire', 'log_max_used', 'log_max_free', 'solve']
    readonly_fields = ['id', ]
    form_layout = (
        Main(
            Tab(
                "日志自动备份",
                Fieldset(
                    "备份设置",
                    Row('auto_backup'),
                    Row('default_backup_crontab', 'default_backup_path'),
                    description="设置自动备份的周期和位置",
                ),
            ),

            Tab(
                "日志阈值设置",
                Fieldset(
                    "",
                    Row('log_expire', ),
                    Row('log_max_free', ),
                    Row('log_max_used', ),
                    description="设置自动备份的周期和位置",
                ),
            ),

        ),
        Side(
            Tab(
                "日志到达阈值的处理",
                Fieldset("", 'solve', ),
            ),
        )
    )

    def show_detail(self, instance):
        pass

    def queryset(self):
        qs = LogMgQuerySet.objects.all()
        if len(qs) < 1:
            _default = LogMgQuerySet()
            _default.save()
        return qs

    def get_context(self):
        context = super(LogMgQuerySetAdmin, self).get_context()
        title = "日志设置"
        context["breadcrumbs"].append({'url': self.get_model_url(AuditPolicyRule, 'changelist'), 'title': '审计策略管理'})
        context["breadcrumbs"].append({'title': title})  # 把面包屑变量添加到context里面
        return context


xadmin.site.register(PasswordQuerySet, PasswordQuerySetAdmin)
xadmin.site.register(LogMgQuerySet, LogMgQuerySetAdmin)
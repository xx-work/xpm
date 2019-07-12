import xadmin
from xadmin.layout import Main, TabHolder, Tab, Fieldset, Row, Col, AppendedText, Side


from ...models import SysManagerCopInfo, ConnectManagerUserInfo, AuditLogObject


class SysManagerCopInfoAdmin(object):
    SelfFound = True

    list_filter = ['type', 'level', ]
    list_display = ['name', 'uniq_flag', 'pushed', 'up', 'ip', 'type', 'level', 'mac', 'os', 'mac_vendor', 'cop_connect_user', 'monitor_agent_config']
    # list_editable = ['uniq_flag', 'ip', 'name', 'pushed']
    show_detail_fields = ('uniq_flag',)

    def cop_connect_user(self, instance):
        show_detaild = lambda x : """<a data-res-uri="{based_url}{id}/detail/" data-edit-uri="{based_url}{id}/update/" 
        class="details-handler" rel="tooltip" title="{name}"> {name}<i class="fa fa-info-circle"></i> </a>  """.format(
            based_url=self.get_model_url(ConnectManagerUserInfo, 'changelist'), id=x.id, name=x.name
        )

        links = "<ul><li>" + "</li><li>".join([show_detaild(x) for x in instance.managers.all()]) + "</li></ul>"
        from django.utils.safestring import mark_safe
        return mark_safe(links)

    cop_connect_user.short_description = "管理员用户集"
    cop_connect_user.allow_tags = True
    cop_connect_user.is_column = True

    def monitor_agent_config(self, instance):
        from agent.models import SnmpAgentCfgInfo
        from mgsd.xadmin.utils.self_utils import get_markd_table_details_show
        try:
            snmp_cfg = SnmpAgentCfgInfo.objects.get(cop=instance)
            return get_markd_table_details_show(url=self.get_model_url(SnmpAgentCfgInfo,
                        'changelist') + str(snmp_cfg.id) + '/detail/', title='配置预览')
        except:
            from mgsd.xadmin.utils.self_utils import mark_safe
            return mark_safe("<a href='{}'>进行配置</a>".format(self.get_model_url(SnmpAgentCfgInfo,
                        'changelist') +'add/?_rel_cop__id__exact=' + str(instance.id)))
    monitor_agent_config.short_description = "SNMP监控配置"

    readonly_fields = ("date_created", "id")
    form_layout = (
        Main(
            Tab(
                "唯一识别标识",
                Fieldset(
                    "唯一识别标识", "uniq_flag", "name", "type",
                    description="系统名称和唯一识别标识",
                ),

            ),
            Tab(
                "平台管理信息",
                Fieldset(
                    "管理用户集", "cop_connect_user",
                    description="管理用户集, 对部件有权限进行系统，安全或者审计管理权限的用户集",
                ),

            ),
            Tab(
                "网络连接信息",
                Fieldset(
                    "IP", "ip", "mac",
                    description="网络拓扑中的信息",
                ),
            ),
            Tab(
                "安全等级",
                Fieldset(
                    "安全等级", "level",
                    description="网络拓扑中的信息",
                ),
            ),

        ),
        Side(
            Tab(
                "状态",
                Fieldset("连接状态", 'pushed', ),
                Fieldset("开机状态", 'up', ),
                # Inline(ActionInline)
            ),
            Tab(
                "硬件信息",
                Fieldset("系统配置", 'os', 'mac_vendor', ),
                # Inline(ActionInline)
            ),

        )
    )

    def save_models(self):
        instance = self.new_obj
        request = self.request

        if request.path.endswith('/add/'):
            instance.pushd = False
        if request.path.endswith('/update/'):
            if request.user.username not in [x.username for x in instance.managers.filter(
                    _identity__in=('sysuser', 'superuser'))]:
                raise ConnectionError('不具备操作权限')

        instance.save()
        flag = self.org_obj is None and 'create' or 'change'
        self.log(flag, self.change_message(), instance)


class ConnectManagerUserInfoAdmin(object):

    list_filter = ['is_active', '_identity', 'create_user',]
    list_display = ['name', 'username', '_password', '_identity', '_protocol', 'is_active', 'create_user', 'date_created', 'see_permissions']
    # list_editable = ['name', 'username', 'process', 'is_active']
    show_bookmarks = False

    def see_permissions(self, instance):
        from mgsd.xadmin.utils.self_utils import get_markd_table_details_show
        # from django.shortcuts import reverse
        return get_markd_table_details_show(url="/admin/group_perm_view", title='查看')
    see_permissions.short_description = "权限视图"

    def save_models(self):
        instance = self.new_obj
        request = self.request

        if request.path.endswith('/add/'):
            from django.contrib.auth.models import User
            all_users = [x.username for x in User.objects.all()]
            if instance.username in all_users:
                if request.path.endwith('update'):
                    raise AssertionError("该用户名已被占用, 请选择独特的用户名或者联系管理员修改平台用户用户名。")

            _user = User(is_active=False, username=instance.username, email=instance.email, is_staff=True)
            _user.set_password(instance._password)
            _user.email = instance.email if instance.email else "test@example.com"
            _user.save()

            instance.create_user = request.user.username
            instance._password = ConnectManagerUserInfo.set_password(instance._password)

        instance.save()
        flag = self.org_obj is None and 'create' or 'change'
        self.log(flag, self.change_message(), instance)

    readonly_fields = ("date_created", "id", 'create_user')
    form_layout = (
        Main(
            Tab(
                "唯一识别标识",
                Fieldset(
                    "唯一识别标识" ,'name',
                    description="系统名称和唯一识别标识",
                ),
            ),
            Tab(
                "用户信息数据集",
                Fieldset(
                    "用户名和密码", 'username',  '_password', '_identity', '_protocol', 'email',
                    description="用户名密码身份以及管理协议",
                ),
            ),
            Tab(
                "密钥和验证相关",
                Fieldset(
                    "web Token", '_token', description="进行http/https管理系统部件时的Web-Token",
                ),
                Fieldset(
                    "ssh公钥私钥", '_public_key', '_private_key', description="普通服务器ssh连接的密钥对。",
                ),
            ),

        ),
        Side(
            Tab(
                "状态",
                Fieldset("连接状态", 'is_active', ),
            ),

            Tab(
                "创建用户和创建时间",
                Fieldset("创建用户", 'create_user', ),
                Fieldset("创建时间", 'date_created', ),
            ),

        )
    )
# 2019-6-22 生产环境下; 一定没有这个 editable 的; 不软不受平台监控。


class AuditLogObjectAdmin(object):

    def cop_connect_user(self, instance):
        show_detaild = lambda x : """<a data-res-uri="{based_url}{id}/detail/" data-edit-uri="{based_url}{id}/update/" 
        class="details-handler" rel="tooltip" title="{name}"> {name}<i class="fa fa-info-circle"></i> </a>  """.format(
            based_url=self.get_model_url(ConnectManagerUserInfo, 'changelist'), id=x.id, name=x.name
        )

        links = "<ul><li>" + "</li><li>".join([show_detaild(x) for x in instance.managers.all()]) + "</li></ul>"
        from django.utils.safestring import mark_safe
        return mark_safe(links)
    cop_connect_user.short_description = "管理员用户集"
    cop_connect_user.allow_tags = True
    cop_connect_user.is_column = True

    list_filter = ['name', 'cop', 'state', ]
    list_display = ['name', 'cop', 'table_name', 'cop_connect_user', 'state', 'date_created']


xadmin.site.register(SysManagerCopInfo, SysManagerCopInfoAdmin)
xadmin.site.register(ConnectManagerUserInfo, ConnectManagerUserInfoAdmin)
xadmin.site.register(AuditLogObject, AuditLogObjectAdmin)

# 注册插件
from .plugins import SystemCopSelfFoundPlugin

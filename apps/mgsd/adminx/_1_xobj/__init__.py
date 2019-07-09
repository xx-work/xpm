import xadmin
from xadmin.layout import Main, TabHolder, Tab, Fieldset, Row, Col, AppendedText, Side
from xadmin.views.base import get_content_type_for_model, ModelAdminView, force_text

from mgsd.models import ChangeAudit

from ...models import SysManagerCopInfo, ConnectManagerUserInfo, AuditLogObject


class SysManagerCopInfoAdmin(ModelAdminView):
    list_filter = ['type', 'level', ]
    list_display = ['name', 'uniq_flag', 'pushed', 'up', 'ip', 'type', 'level', 'mac', 'os', 'mac_vendor', 'cop_connect_user']
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


class ConnectManagerUserInfoAdmin(object):

    list_filter = ['is_active', '_identity', 'create_user',]
    list_display = ['name', 'username', '_password', '_identity', '_protocol', 'is_active', 'create_user', 'date_created']
    list_editable = ['name', 'username', 'process', 'is_active']
    show_bookmarks = False

    def save_models(self):
        instance = self.new_obj
        request = self.request

        from django.contrib.auth.models import User
        all_users = [x.username for x in User.objects.all()]
        if instance.username in all_users:
            if request.META["url"].endwith('update'):
                raise AssertionError("该用户名已被占用, 请选择独特的用户名或者联系管理员修改平台用户用户名。")

        # from django.contrib.auth.hashers import (
        #     check_password, is_password_usable, make_password,
        # )

        _user = User(is_active=False, username=instance.username, email=instance.email, is_staff=True)
        _user.set_password(instance._password)
        _user.email = instance.email if instance.email else "test@example.com"
        _user.save()

        instance.create_user = request.user.username
        instance._password = ConnectManagerUserInfo.set_password(instance._password)

        instance.save()

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
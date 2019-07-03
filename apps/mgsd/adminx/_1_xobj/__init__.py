import xadmin

from ...models import SysManagerCopInfo, ConnectManagerUserInfo, AuditLogObject

from django.http import HttpResponse


class SysManagerCopInfoAdmin(object):
    list_filter = ['type', 'level', ]
    list_display = ['name', 'uniq_flag', 'pushed', 'up', 'ip', 'type', 'level', 'mac', 'os', 'mac_vendor']
    list_editable = ['uniq_flag', 'ip', 'name', 'pushed']


class ConnectManagerUserInfoAdmin(object):

    list_filter = ['is_active', '_identity', 'create_user',]
    list_display = ['name', 'username', '_password', '_identity', '_protocol', 'is_active', 'create_user', 'date_created']
    list_editable = ['name', 'username', 'process', 'is_active']

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
# 2019-6-22 生产环境下; 一定没有这个 editable 的; 不软不受平台监控。


xadmin.site.register(SysManagerCopInfo, SysManagerCopInfoAdmin)
xadmin.site.register(ConnectManagerUserInfo, ConnectManagerUserInfoAdmin)
xadmin.site.register(AuditLogObject)
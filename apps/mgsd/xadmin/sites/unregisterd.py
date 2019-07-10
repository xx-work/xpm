import xadmin

# from django_celery_beat.models import PeriodicTask, CrontabSchedule, IntervalSchedule
# xadmin.sites.register(PeriodicTask)
# xadmin.sites.register(CrontabSchedule)
# xadmin.sites.register(IntervalSchedule)


class HideMenuAdmin(object):
    hidden_menu = True


from reversion.models import Revision

# 取消注册Revision
from xadmin.plugins.xversion import ReversionAdmin


class ReversionAdmin2(ReversionAdmin, HideMenuAdmin):
    pass
xadmin.site.unregister(Revision)
xadmin.site.register(Revision, ReversionAdmin2)


from django.contrib.auth.models import (User, Permission, Group)


from xadmin.plugins.auth import GroupAdmin, UserAdmin, PermissionAdmin

# 菜单掩盖
class UserAdmin2(HideMenuAdmin, UserAdmin):
    pass
xadmin.site.unregister(User)
xadmin.site.register(User, UserAdmin2)


class GroupAdmin2(HideMenuAdmin, GroupAdmin):
    pass
xadmin.site.unregister(Group)
xadmin.site.register(Group, GroupAdmin2)


class PermissionAdmin2(HideMenuAdmin, PermissionAdmin):
    pass
xadmin.site.unregister(Permission)
xadmin.site.register(Permission, PermissionAdmin2)




import xadmin


from ...models import BackUpHistory


class BackUpHistoryAdmin(object):
    backup_plugin = True

    list_display = ("backup_type", "backup_path", "backup_host", "opreate_username", "date_created")

    # 后面在这里接纳一个函数能够直接进行点击备份和恢复。
    readonly_fields = ("opreate_username", )

    def save_models(self):
        instance = self.new_obj
        request = self.request

        if not instance.opreate_username:
            instance.opreate_username = request.user.username
        instance.save()


xadmin.site.register(BackUpHistory, BackUpHistoryAdmin)

from .plugin import *




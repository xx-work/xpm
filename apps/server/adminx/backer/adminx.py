import xadmin


from ...models import BackUpHistory


class BackUpHistoryAdmin(object):
    list_display = ("backup_type", "backup_path", "backup_host", "opreate_username", "date_updated")


xadmin.site.register(BackUpHistory, BackUpHistoryAdmin)







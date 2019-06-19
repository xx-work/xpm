import xadmin

from ...models import InfoSecEvent, InfoGoin, EffectInfo, AttackerActionDesc


class InfoSecEventAdmin(object):
    list_display = ['infosysname', 'info_type', 'describtion', 'info_level', 'descover_time', 'happend_time', 'report_time']


xadmin.site.register(InfoSecEvent, InfoSecEventAdmin)

xadmin.site.register(EffectInfo)
xadmin.site.register(AttackerActionDesc)
xadmin.site.register(InfoGoin)

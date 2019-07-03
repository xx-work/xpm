# coding:utf-8

### 将所以消息标记为已处理

from xadmin.plugins.actions import BaseActionView
from django.http import HttpResponse


class ViewdAction(BaseActionView):

    # 这里需要填写三个属性
    action_name = "change_to_viewd"
    description = u'标记为跟进中 %(verbose_name_plural)s'
    model_perm = 'change'

    def do_action(self, queryset):
        for obj in queryset:
            from mgsd.models import InfoGoin
            InfoGoin.objects.create(info=obj, had_action='已有前例。', state='ING', go_user='system001')
        return HttpResponse('标记完成')
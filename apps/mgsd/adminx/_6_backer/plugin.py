from django.template import loader

from mgsd.xadmin.utils.hockd_utils import get_context_dict

from xadmin.views import BaseAdminPlugin, ListAdminView
from xadmin.views.base import filter_hook

from django.shortcuts import reverse

# 显示插件 https://www.cnblogs.com/lanqie/p/8340215.html
class BackupButtonPlugin(BaseAdminPlugin):
    backup_plugin = False

    def init_request(self, *args, **kwargs):
        return self.backup_plugin

    def block_top_toolbar(self, context, nodes):
        _context = dict(
            button_url=reverse('backup'),
            buttom_title='进行备份操作'
        )
        context = dict(context, **_context)
        nodes.append(loader.render_to_string("cso/plugins/top_toolbar.html", get_context_dict(context)))

    # 使用此装饰器来装饰方法表示该方法可以被插件截获或者修改
    # @filter_hook
    # def get_context(self, context):
    #     context.update({'hello_target': 'World!!'})
    #     return context

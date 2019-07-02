from django.template import loader

from manager.xadmin.utils.hockd_utils import get_context_dict

from xadmin.views import BaseAdminPlugin
from xadmin.views.base import filter_hook


# 显示插件 https://www.cnblogs.com/lanqie/p/8340215.html
class ListReturndPlugin(BaseAdminPlugin):
    # isExecute = False

    def init_request(self, *args, **kwargs):
        return self.request.get_full_path().endswith('data/')
        # return self.request.get_full_path().endswith('data/') or self.isExecute

    def block_top_toolbar(self, context, nodes):
        nodes.append(loader.render_to_string("cso/plugins/top_toolbar.html", get_context_dict(context)))

    # 使用此装饰器来装饰方法表示该方法可以被插件截获或者修改
    # @filter_hook
    def get_context(self, context):
        context.update({'hello_target': 'World!!'})
        return context


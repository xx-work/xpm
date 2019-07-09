from django.template import loader

from mgsd.xadmin.utils.hockd_utils import get_context_dict

from xadmin.views import BaseAdminPlugin, ListAdminView
from xadmin.views.base import filter_hook


# 显示插件 https://www.cnblogs.com/lanqie/p/8340215.html
class SystemCopSelfFoundPlugin(BaseAdminPlugin):
    SelfFound = False

    def init_request(self, *args, **kwargs):
        return bool(self.SelfFound)

    def block_top_toolbar(self, context, nodes):
        nodes.append(loader.render_to_string("cso/plugins/system_cop_identify.html", get_context_dict(context)))

    # 使用此装饰器来装饰方法表示该方法可以被插件截获或者修改
    # @filter_hook
    def get_context(self, context):
        context.update({'alert_msg': '扫描已经开始'})
        return context


import xadmin
xadmin.site.register_plugin(SystemCopSelfFoundPlugin, ListAdminView)


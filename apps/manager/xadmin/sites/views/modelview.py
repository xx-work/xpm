
from xadmin.views.base import ModelAdminView, filter_hook, csrf_protect_m
from xadmin.views import BaseAdminView

from agent.adminx import SnmpAgentCfgInfoAdmin
from ..nav_menu_lists import GlobalSetting
# from agent.



class CommAdminView(object):

    @filter_hook
    def get_context(self):
        super(SnmpAgentCfgInfoAdmin, self).get_context()
        nav_menu = GlobalSetting().get_site_menu()

        for menu in nav_menu:
            check_selected(menu, self.request.path)

        # 添加自定义url,视图函数获取数据
        add_url_flag = False
        auto_title = ''
        pid = ''
        subtitle = ''
        print(self.request.get_full_path())
        if '/xadmin/cashflows/cash_title_content/' in self.request.get_full_path():
            from apps.cashflows.models import cash_title_link, cash_title_content
            add_url_flag = True
            auto_title = cash_title_link.objects.all()
            # print('title', title)
            pid = self.request.GET.get('pid')
            # print('pid', pid, type(pid))
            if pid:
                subtitle = cash_title_content.objects.filter(content_cash_id=pid)
                pid = int(pid)
            else:
                subtitle = None
        else:
            pass
        context = super().get_context()
        print('auto_title', auto_title)
        print('pid', pid)
        print('subtitle', subtitle)
        context.update({
            'menu_template': self.menu_template,
            'nav_menu': nav_menu,
            'site_title': self.site_title,
            'site_footer': self.site_footer,
            'breadcrumbs': self.get_breadcrumb(),

            # 自定义获取的数据，返回给base_site.html页面
            'add_url_flag': add_url_flag,
            'auto_title': auto_title,
            'subtitle': subtitle,
            'pid': pid,
        })

        return context

    # def get_context(self):
    #     context = super(SimCardServicesAdmin, self).get_context()
    #     f = context.get('form', None)
    #     if f:
    #         card_id = f['card'].value()
    #         card_info_obj = SimCardInfo.objects.get(card=card_id)
    #         card_info_form = SimCardInfoForm(instance=card_info_obj)　　　　　　　
    #         helper = self.get_form_helper()
    #         layout = Layout(Container(
    #             Col('full', Fieldset("", *card_info_form.fields.keys(), css_class="unsort no_title"), horizontal=True,
    #                 span=12)))
    #         setattr(helper, 'layout', layout)
    #
    #         setattr(card_info_form, 'helper', helper)
    #         # setattr(card_info_form, 'helper', self.get_form_helper())
    #         pdb.set_trace()
    #         context.update({'form2': card_info_form})
    #     return context
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
try:
    from django.core.urlresolvers import reverse
except:
    from django.urls import reverse
# Create your views here.


def homepage(request):
    return HttpResponseRedirect(reverse('dashboard'))


def dashboard(request):
    return render(request, 'cso/index.html')


import xadmin
from xadmin.views import CommAdminView


class TestInputView(CommAdminView):

    def get(self, request, pk):
        context = super().get_context()
        title = "BootStrap测试"  # 定义面包屑变量
        context["breadcrumbs"].append({'url': '/', 'title': '首页'})  # 把面包屑变量添加到context里面
        context["breadcrumbs"].append({'title': title})  # 把面包屑变量添加到context里面
        context.update({"private_key": pk})
        return render(request, 'cso/xadmin/demo.html', context)


from mgsd.url_confs import MEMU_SUFFIX, get_menu_origin_url, get_menu_url


class MenuAttackOneToRedirectView(CommAdminView):

    def get(self, request, pk):
        # from website.settings import SITE_URL
        # import requests
        # content = requests.get(SITE_URL + get_menu_origin_url(pk)).content
        #
        # return HttpResponse(content)
        return redirect( get_menu_origin_url(pk) )


xadmin.site.register_view(r'^' + MEMU_SUFFIX + '(?P<pk>[\w_]+)$', MenuAttackOneToRedirectView, name='menu_url_kv')
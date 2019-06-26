from django.shortcuts import render

from xadmin.views import CommAdminView


class SystemCentralManagementsView(CommAdminView):
    def get(self, request):
        context = super().get_context()  # 这一步是关键，必须super一下继承CommAdminView里面的context，不然侧栏没有对应数据，我在这里卡了好久
        title = "系统策略集中管理"  # 定义面包屑变量
        context["breadcrumbs"].append({'url': '/admin', 'title': '系统部件管理'})  # 把面包屑变量添加到context里面
        context["breadcrumbs"].append({'url': '/admin', 'title': title})  # 把面包屑变量添加到context里面

        context["title"] = title  # 把面包屑变量添加到context里面

        # 下面你可以接着写你自己的东西了，写完记得添加到context里面就可以了
        context["messages"] = [{'tags': "info", 'alert-info': "消息" + str(i)} for i in range(3)]

        return render(request, 'cso/xadmin/base_site.html', context)  # 最后指定自定义的template模板，并返回context


class TestEchartsView(CommAdminView):

    def get(self, request):
        context = super().get_context()
        title = "Echarts测试"  # 定义面包屑变量
        context["breadcrumbs"].append({'url': '/', 'title': '首页'})  # 把面包屑变量添加到context里面
        context["breadcrumbs"].append({'title': title})  # 把面包屑变量添加到context里面

        return render(request, 'cso/xadmin/audit/echarts_show.html', context)  # 最后指定自定义的template模板，并返回context
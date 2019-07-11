from django.shortcuts import render

from xadmin.views import CommAdminView
from django.contrib.auth.models import Group


class GroupPermissionView(CommAdminView):

    def get(self, request):
        group_id = int(request.GET['group_id'])
        _group = Group.objects.get(id=group_id)
        context = super().get_context()
        title = "用户组权限管理"  # 定义面包屑变量
        context["breadcrumbs"].append({'url': '/', 'title': '首页'})  # 把面包屑变量添加到context里面
        context["breadcrumbs"].append({'title': title})  # 把面包屑变量添加到context里面

        from mgsd.api.policy.policydetails.group_perm_views import get_group_perm_view_table
        render_str = get_group_perm_view_table()

        context.update({'render_txt': render_str})

        return render(request, 'cso/xadmin/demo.html', context)


import xadmin
xadmin.site.register_view(r'^group_perm_view', GroupPermissionView, name='group_perm_view')
from django.shortcuts import render, redirect, reverse

from xadmin.views import CommAdminView

from mgsd.models import SysManagerCopInfo


class SelfFoundThenRedictView(CommAdminView):
    def get(self, request):
        context = super().get_context()
        return redirect(self.get_model_url(SysManagerCopInfo, 'changelist'))


import xadmin
xadmin.site.register_view(r'^system_cop_found', SelfFoundThenRedictView, name='selfound')
# coding:utf-8
from django.shortcuts import redirect, reverse

from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes

from xadmin.models import Log
# from xadmin.views import BaseAdminView, CreateAdminView

from mgsd.api.xobj.models import SysManagerCopInfo, ConnectManagerUserInfo, AuditLogObject
# from mgsd.api.solution.models import InfoSecEvent
from mgsd.xtool.chks.tools import cop_chk_2_infosec, aud_chk_2_infosec, user_chk_2_infosec


@api_view(['GET'])
@permission_classes((IsAuthenticated, ))
def push2infosec(request):
    http_reffer = request.META['HTTP_REFERER']

    logid = request.GET['id']
    _log = Log.objects.get(id=logid)
    flug = True
    while True:
        ModelObj = _log.content_type.model_class()
        _obj = ModelObj.objects.get(id=_log.object_id)
        if ModelObj == SysManagerCopInfo:
            cop_chk_2_infosec(_obj)
            break
        if ModelObj == ConnectManagerUserInfo:
            user_chk_2_infosec(_obj)
            break
        if ModelObj == AuditLogObject:
            aud_chk_2_infosec(_obj)
            break
        flug = False
        break
    if flug:
        # return Response({"state": True, "reason": "已经进入到响应处置阶段"})
        return redirect(http_reffer)
    else:
        # return Response({"state": False, "reason": "对象不存在, 或者参数错误"}, status=204)
        return Response({"state": False, "reason": "对象不存在, 或者参数错误"}, status=204)











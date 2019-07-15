# coding:utf-8
import json
from django.http import JsonResponse
from rest_framework.response import Response

from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes

@api_view(['POST'])
@permission_classes(())
def push_pot_data_to_cso_alerts(request):
    from .potlog2cso import pot2cso, POT_IP, POT_USERNAME
    data = request.data

    if request.META["REMOTE_ADDR"] not in [POT_IP, '127.0.0.1', 'localhost', ]:
        return Response({"stat": False, "reason":"数据源不正确"})

    if "auth_username" not in data.keys() or "auth_passwd" not in data.keys():
        return Response({"stat": False, "reason":"缺少必须的auth认证"})

    if data["auth_username"] not in [POT_USERNAME, ] or data["auth_passwd"] != '112233..':
        return Response({"stat": False, "reason" : "Auth认证失败"})

    descover_time=data["descover_time"] if "descover_time" in data.keys() else None
    happend_time=data["happend_time"] if "descover_time" in data.keys() else None
    extra=data["extra"] if "extra" in data.keys() else None
    infosysname=data["infosysname"] if "infosysname" in data.keys() else None
    advice=data["advice"] if "advice" in data.keys() else None
    summary=data["advice"] if "advice" in data.keys() else None
    info = pot2cso(descover_time=descover_time, happend_time=happend_time,
        infosysname=infosysname, extra=extra, summary=summary, advice=advice, auth_username=data["auth_username"])

    return Response({"stat": True, "data": data})

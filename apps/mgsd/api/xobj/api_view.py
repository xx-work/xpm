# coding:utf-8
from rest_framework.response import Response

from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes


@api_view(['GET'])
@permission_classes((IsAuthenticated, ))
def copfound(request):
    return Response({"stat": True, "reason": "自发现任务执行中。"})


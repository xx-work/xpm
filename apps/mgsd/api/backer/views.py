# coding:utf-8
from rest_framework.response import Response

from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes


@api_view(['GET'])
@permission_classes((IsAuthenticated, ))
def backup(request):
    return Response({"stat": True, "reason": "备份成功"})


@api_view(['POST'])
@permission_classes((IsAuthenticated, ))
def recover(request):
    return Response({"stat": True, "reason": "备份成功"})
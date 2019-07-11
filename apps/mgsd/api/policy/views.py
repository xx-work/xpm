# coding:utf-8
from rest_framework.response import Response

from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes


@api_view(['GET'])
@permission_classes((IsAuthenticated, ))
def password_policy(request):
    pass


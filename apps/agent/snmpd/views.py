# coding:utf-8
import json
from django.http import JsonResponse
from rest_framework.response import Response

# from django.forms.models import model_to_dict
from django.core.paginator import Paginator

from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes

# from secs.utils.db_utils import from_sql_get_data


@api_view(['GET'])
# @permission_classes((IsAuthenticated, ))
def collect_data(request):
    from agent.tasks import sysdatas2db
    sysdatas2db.delay()
    return Response({"stat": True, "sync": "同步基本数据库信息已经执行"}, status=201)


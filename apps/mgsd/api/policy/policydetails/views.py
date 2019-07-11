# coding:utf-8
from django.shortcuts import reverse, redirect

from rest_framework.response import Response

from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes

from .models import PasswordQuerySet, LogMgQuerySet
# from .adminx import PasswordQuerySetAdmin, LogMgQuerySetAdmin


@api_view(['GET'])
@permission_classes((IsAuthenticated, ))
def get_latest_password_policy(request):
    _obj = PasswordQuerySet.objects.all().order_by('-date_created')[0]
    url = "/admin/mgsd/passwordqueryset/" + str(_obj.id) + "/detail/"
    return redirect(url)


@api_view(['GET'])
@permission_classes((IsAuthenticated, ))
def get_latest_log_policy(request):
    _obj = LogMgQuerySet.objects.all().order_by('-date_created')[0]
    # url = LogMgQuerySetAdmin().get_model_url(model=LogMgQuerySet, name='changelist') + str(_obj.id) + "/detail/"
    url = "/admin/mgsd/logmgqueryset/" + str(_obj.id) + "/detail/"
    return redirect(url)
# coding:utf-8
from uuid import uuid4
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes

from .conf import get_backup_recover_cmd, MYSQL_DB_BACKUPD_PATH
from ..models import BackUpHistory


@api_view(['POST'])
@permission_classes((IsAuthenticated, ))
def backup_plat_db(request):
    uid = uuid4()
    try:
        BackUpHistory.objects.create(
            id=uid,
            opreate_username=request.user.username,
            backup_path=MYSQL_DB_BACKUPD_PATH(uid),
            backup_type="backup"
        )
        try:
            return Response({"reason": "BackUp Sucess", "stat": True})
        finally:
            get_backup_recover_cmd(uid=uid)
    except:
        import logging
        logging.error("备份数据库失败")
        return Response({"reason": "BackUp Faild", "stat": False})


@api_view(['POST'])
@permission_classes((IsAuthenticated, ))
def recover_plat_db(request):
    # 当前备份的事件ID
    uid = request.POST["uid"]
    try:
        BackUpHistory.objects.create(
            id=uid,
            opreate_username=request.user.username,
            backup_path = MYSQL_DB_BACKUPD_PATH(uid),
            backup_type = "recover"
        )
        try:
            return Response({"reason": "recover Sucess", "stat": True})
        finally:
            get_backup_recover_cmd(uid=uid)

    except:
        import logging
        logging.error("备份数据库失败")
        return Response({"reason": "recover Faild", "stat": False})




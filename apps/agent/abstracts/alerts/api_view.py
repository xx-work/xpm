# coding:utf-8
# import json
# from django.http import JsonResponse
from rest_framework.response import Response
# from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes


@api_view(['POST'])
@permission_classes(())
def push_single_pot_data_to_cso_alerts(request):
    from .potlog2cso import pot2cso, POT_IP, POT_USERNAME, load_cop_user, user_sig_is_ture, PublicKey, PrivateKey
    data = request.data

    if request.META["REMOTE_ADDR"] not in [POT_IP, '127.0.0.1', 'localhost', ]:
        return Response({"stat": False, "reason":"数据源不正确"})

    if "auth_username" not in data.keys() or "auth_passwd" not in data.keys():
        return Response({"stat": False, "reason":"缺少必须的auth认证"})

    if data["auth_username"] not in [POT_USERNAME, ] or data["auth_passwd"] != '112233..':
        return Response({"stat": False, "reason" : "Auth认证失败"})

    try:
        sig = request.FILES.get('sig')
        global signature
        signature = sig.open('rb').read()
    except:
        return Response({"stat": False, "reason": "sig签名证书文件丢失。"})

    _conn_user = load_cop_user()
    state = user_sig_is_ture(sig=signature, _public_key=_conn_user._public_key)

    if not state:
        return Response({"stat": False, "reason": "签名证书有误！"})

    descover_time=data["descover_time"] if "descover_time" in data.keys() else None
    happend_time=data["happend_time"] if "descover_time" in data.keys() else None
    extra=data["extra"] if "extra" in data.keys() else None
    infosysname=data["infosysname"] if "infosysname" in data.keys() else None
    advice=data["advice"] if "advice" in data.keys() else None
    summary=data["advice"] if "advice" in data.keys() else None
    info = pot2cso(descover_time=descover_time, happend_time=happend_time,
        infosysname=infosysname, extra=extra, summary=summary, advice=advice, auth_username=data["auth_username"])

    return Response({"stat": True, "data": '====='})


@api_view(['POST'])
@permission_classes(())
def push_pot_data_to_cso_alerts(request):
    from .potlog2cso import pot2cso, POT_IP, POT_USERNAME, load_cop_user, user_sig_is_ture, PublicKey, PrivateKey
    data = request.data

    if request.META["REMOTE_ADDR"] not in [POT_IP, '127.0.0.1', 'localhost', '192.168.2.227', '192.168.2.161']:
        return Response({"stat": False, "reason":"数据源不正确"})

    if "auth_username" not in data.keys() or "auth_passwd" not in data.keys():
        return Response({"stat": False, "reason":"缺少必须的auth认证"})

    if data["auth_username"] not in [POT_USERNAME, ] or data["auth_passwd"] != '112233..':
        return Response({"stat": False, "reason" : "Auth认证失败"})

    try:
        sig = request.FILES.get('sig')
        global signature
        signature = sig.open('rb').read()
    except:
        return Response({"stat": False, "reason": "sig签名证书文件丢失。"})

    _conn_user = load_cop_user()
    state = user_sig_is_ture(sig=signature, _public_key=_conn_user._public_key)

    if not state:
        return Response({"stat": False, "reason": "签名证书有误！"})

    _all_lists = data["alerts"] if "alerts" in data.keys() else None

    from agent.tasks import miguan_alerts_tasks
    miguan_alerts_tasks.delay(_all_lists=_all_lists, data=data)

    return Response({"stat": True, "data": data["alerts"], "result": "完成"})


def alerts_input_tasks(_all_lists, data):
    from .potlog2cso import pot2cso, POT_IP, POT_USERNAME, load_cop_user, user_sig_is_ture, PublicKey, PrivateKey
    results = []
    for alert in _all_lists:
        try:
            descover_time=alert["descover_time"] if "descover_time" in alert.keys() else None
            happend_time=alert["happend_time"] if "descover_time" in alert.keys() else None
            extra=alert["extra"] if "extra" in alert.keys() else None
            infosysname=alert["infosysname"] if "infosysname" in alert.keys() else None
            advice=alert["advice"] if "advice" in alert.keys() else None
            summary=alert["advice"] if "advice" in alert.keys() else None
            slug, _ = pot2cso(descover_time=descover_time, happend_time=happend_time,
                infosysname=infosysname, extra=extra, summary=summary, advice=advice, auth_username=data["auth_username"])
            results.append((slug, '导入' + infosysname + "secucess"))
        except:
            results.append((False, '导入格式错误'))
    return results


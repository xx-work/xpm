from src import django_setup


audit_logs = [
   [ '登录日志', 'login_log',],
       [ '登录日志', 'login_log',],
    ['平台变更日志', 'chk_log',],
     ['响应事件日志', 'info_event',],
      [ '系统监控日志', 'process',],
]


def inital_auditlog():
    django_setup()

    from mgsd.models import AuditLogObject, SysManagerCopInfo, ConnectManagerUserInfo

    for alog in audit_logs:
        ao = AuditLogObject(name=alog[0],
                      cop = SysManagerCopInfo.objects.get(uniq_flag='cya_cso_6000_v1'),
                     table_name=alog[1])
        ao.save()
        ao.managers.add(ConnectManagerUserInfo.objects.get(username='admin001'))

    print("初始化审计对象结束。")


if __name__ == '__main__':

    inital_auditlog()
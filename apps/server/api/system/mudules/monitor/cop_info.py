from cso.models import (
    SysManagerCopInfo, HostService, ConnectManagerUserInfo
)


def create_cop_default_user(name="普通KVM默认用户", username="root", password="111111"):
    _lists = ConnectManagerUserInfo.objects.filter(name = name,
        username = username,
        _password = password,)

    if len(_lists) > 0:
        return _lists[0]

    _user = ConnectManagerUserInfo.objects.create(
        name = name,
        username = username,
        _password = password,
    )
    return _user
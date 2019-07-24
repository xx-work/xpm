import rsa
from src import django_setup
django_setup()


if __name__ == '__main__':
    from agent.api.interceptors.request_ips import IpsRequestMiddleHandle
    from agent.api.devices.agent_api import IPS_API
    resp1 = IpsRequestMiddleHandle.refrash_token_and_userinfo()
    # print(resp)
    # IpsRequestMiddleHandle.refrash_c_tokenid()

    resp = IpsRequestMiddleHandle(
        url='/bg/sysutil/sysconf/' + str(IPS_API.get_token())
    ).request()

    print(resp.text)


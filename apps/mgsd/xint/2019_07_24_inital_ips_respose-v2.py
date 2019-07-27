import rsa
from src import django_setup
django_setup()


def test2():
    from agent.api.devices.ips.fips.intercepter import IpsRequestMiddleHandle
    # resp1 = IpsRequestMiddleHandle.refrash_token_and_userinfo()
    # print(resp1)
    # IpsRequestMiddleHandle.refrash_c_tokenid()

    ## test_any_jk

    from agent.models import AgentApi
    for x in AgentApi.objects.filter(method='get'):

        resp = IpsRequestMiddleHandle(url=x.url, method=x.method, auth=x.auth).fetch()
        print(resp)


def test1():
    from agent.api.devices.ips.fips.intercepter import IpsRequestMiddleHandle
    resp1 = IpsRequestMiddleHandle.refrash_token_and_userinfo()
    print(resp1)
    # IpsRequestMiddleHandle.refrash_c_tokenid()


if __name__ == '__main__':
    test2()






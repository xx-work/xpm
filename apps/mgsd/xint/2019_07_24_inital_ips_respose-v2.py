import rsa
from src import django_setup
django_setup()


if __name__ == '__main__':
    from agent.api.devices.ips.fips.intercepter import IpsRequestMiddleHandle
    resp1 = IpsRequestMiddleHandle.refrash_token_and_userinfo()
    print(resp1)
    # IpsRequestMiddleHandle.refrash_c_tokenid()



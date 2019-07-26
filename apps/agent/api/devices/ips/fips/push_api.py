import requests
import json

_CUSTOM_TOKEN_ID = 'iVqFs8jC550jrphTiOu9goEtumxQLNRi'
_IPS_LOGIN_URL = "https://192.168.2.10/auth/sign"


def get_ips_token(ips_username='aq009',
                  ips_password='999999',
                  ips_token=_CUSTOM_TOKEN_ID):
    """
    链接IPS的登录接口的接口; 使用requests
    :param ips_username:
    :param ips_password:
    :param ips_token:
    :return:
    """
    resp = requests.post(_IPS_LOGIN_URL,
                         data={'username': ips_username, "password": ips_password},
                         headers={'C-TOKEN-ID': ips_token},
                         verify=False)
    result = json.loads(resp.text)
    if result["status"] == "0":
        token = result["results"][0]
        identity = result["results"][1]
        return token, identity
    return None


if __name__ == '__main__':
    data = get_ips_token()
    print(data)
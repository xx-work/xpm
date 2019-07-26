# import requests
import json
from requests.api import request

from ..devices.agent_api import IPS_API
from ..utils.request_default_headers import ips_headers


class IpsRequestMiddleHandle():

    def __init__(self, method='get', url=None, token=None, data=None, headers=None):
        self.method = method
        self.url = url
        self.token = token
        self.data = data
        if headers:
            self.headers = headers
        else:
            self.headers = ips_headers

    @staticmethod
    def refrash_c_tokenid():
        resp = IpsRequestMiddleHandle(
            url='/login.html',
            headers={'User-Agent': "CSO-Test-Backend-v0.1"}
        )
        resp = resp.request().text
        import re
        try:
            c_token_id = re.findall("""headers:{'C-TOKEN-ID':'(.*?)'}""", resp)[0]
        except:
            c_token_id = None
        return c_token_id

    @staticmethod
    def refrash_token_and_userinfo():
        username, password = IPS_API.default_user
        resp = IpsRequestMiddleHandle(
            method='post',
            url=IPS_API.login_url,
            token=None,
            data={'username': username, 'password': password},
            headers=None
        ).request()
        datas = json.loads(resp.text)
        token, role = datas["results"]
        from ..devices.ips.user_role import IPS_ROLE_KV
        userinfo = {"username": username, role: IPS_ROLE_KV[str(role)]}
        IPS_API.set_token(token)
        IPS_API.set_userinfo(userinfo)
        return token, userinfo

    def request(self, token=None):
        resp = request(method=self.method,
                       url=IPS_API.scheme + self.url,
                       data=self.data,
                       headers=self.headers,
                       verify=False)
        json_response = json.loads(resp.text)
        if "msg" in json_response.keys():
            print(json_response["msg"])
            print('=========================')
            print(resp.url)
        return resp

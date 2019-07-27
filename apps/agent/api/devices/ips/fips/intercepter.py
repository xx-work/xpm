# import requests
import json
from requests.api import request
from django.core.cache import cache
# from agent.api.devices.ips.fips.api import IPS_API
from agent.api.devices.models import AgentApi, SysManagerCopInfo
from agent.api.devices.ips.settings import IPS_DEFAULT_REQUEST_HEADERS, IPS_ROLE_KV


class IpsRequestMiddleHandle(object):
    TOKEN_SUFFIX = '_token'
    USERINFO_SUFFIX = '_userinfo'

    def __init__(self, method='get', url=None, data=None, headers=None, auth=True):
        self.method = method
        self.url = url
        self.data = data
        self.auth = auth
        if headers:
            self.headers = headers
        else:
            self.headers = IPS_DEFAULT_REQUEST_HEADERS

    def todict(self):
        return dict(
            url=self.url,
            method=self.method,
            data=self.data,
            headers=self.headers,
            auth=self.auth,
        )

    @staticmethod
    def local_ips_cop():
        return SysManagerCopInfo.objects.get(uniq_flag='ips_cya_0726')

    @staticmethod
    def refrash_c_tokenid():
        resp = IpsRequestMiddleHandle(
            url='/login.html',
            headers={'User-Agent': "CSO-Test-Backend-v0.1"}
        )
        resp = resp.fetch().text
        import re
        try:
            c_token_id = re.findall("""headers:{'C-TOKEN-ID':'(.*?)'}""", resp)[0]
        except:
            c_token_id = None
        return c_token_id

    @staticmethod
    def refrash_token_and_userinfo():
        _login_api = AgentApi.objects.filter(agent=IpsRequestMiddleHandle.local_ips_cop(), _type='login')[0]

        try:
            cop_manager = _login_api.agent.managers.all().filter(_identity='superuser', is_active=True)[0]
        except:
            raise EnvironmentError('系统部件连接出错, 需要检验部件信息和连接的特权管理员')
        username, password = cop_manager.username, cop_manager._password
        datas = IpsRequestMiddleHandle(
            method='post',
            url=_login_api.url,
            data={'username': username, 'password': password},
            headers=None,
            auth=False
        ).fetch()
        token, role = datas["results"]

        userinfo = {"username": username, role: IPS_ROLE_KV[str(role)]}
        # 保存cache
        IpsRequestMiddleHandle.set_token(token)
        IpsRequestMiddleHandle.set_userinfo(userinfo)

        return token, userinfo

    @staticmethod
    def set_token(token):
        cop = IpsRequestMiddleHandle.local_ips_cop()
        return cache.set(cop.uniq_flag + IpsRequestMiddleHandle.TOKEN_SUFFIX, token)

    @staticmethod
    def set_userinfo(userinfo):
        cop = IpsRequestMiddleHandle.local_ips_cop()
        return cache.set(cop.uniq_flag + IpsRequestMiddleHandle.USERINFO_SUFFIX, userinfo)

    @staticmethod
    def get_token():
        cop = IpsRequestMiddleHandle.local_ips_cop()
        return cache.get(cop.uniq_flag + IpsRequestMiddleHandle.TOKEN_SUFFIX)

    @staticmethod
    def get_conn_userinfo():
        cop = IpsRequestMiddleHandle.local_ips_cop()
        return cache.get(cop.uniq_flag + IpsRequestMiddleHandle.USERINFO_SUFFIX)

    def fetch(self, token=None):
        fetch_url = self.local_ips_cop().prefix + self.url
        if self.auth:
            if not token:
                token = IpsRequestMiddleHandle.get_token()
                if not token:
                    self.refrash_token_and_userinfo()
                    token = IpsRequestMiddleHandle.get_token()

            fetch_url = fetch_url + token
        resp = request(method=self.method,
                       url=fetch_url,
                       data=self.data,
                       headers=self.headers,
                       verify=False
                       )
        try:
            json_response = json.loads(resp.text)
            print(json_response)
        except:
            print("非Json返回的内容;不做处理，直接返回Response")
            return resp
        if "status" in json_response.keys():
            # https://192.168.2.188/ips_develop_group/rbac_sys#%E8%BF%94%E5%9B%9E%E7%8A%B6%E6%80%81%E5%80%BC
            if int(json_response["status"]) in [0, ]:
                return json_response
            else:
                if int(json_response["status"]) == 4:
                    # 认证失败, 重新签发
                    self.refrash_token_and_userinfo()
                    _self = self.todict()
                    _self["token"] = IpsRequestMiddleHandle.get_token()
                    return IpsRequestMiddleHandle(**_self).fetch(token=_self["token"])

                from ..settings import IPS_ERROR_RESPONSE
                return {"reason": IPS_ERROR_RESPONSE[json_response["status"]], 'state': False}
        return json_response
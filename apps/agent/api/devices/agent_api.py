from django.core.cache import cache
# from ...api.utils.rediscli import RedisCli
# cache = RedisCli().redis_agent()


class DeiviceApiQs():

    def __init__(self, scheme, login_url, logout_url, user_info_url, user_list_url, login_cfg_url, white_urls=None, device_type='ips', default_user=['admin', 'admin']):
        self.scheme = scheme
        self.login_url = login_url
        self.logout_url = logout_url
        self.user_list_url = user_list_url
        self.user_info_url = user_info_url
        self.login_cfg_url = login_cfg_url
        self.white_urls = white_urls
        self.device_type = device_type
        if not white_urls:
            self.white_urls = [login_url, ]
        self.default_user = default_user

    def set_token(self, token):
        cache.set(self.device_type + '_token', token)

    def get_token(self):
        return cache.get(self.device_type + '_token')

    def set_userinfo(self, userinfo):
        cache.set(self.device_type + '_userinfo', userinfo)

    def get_user_info(self):
        return cache.get(self.device_type + '_userinfo')


# 目前这个是写死的状态, 但是后期都是从数据库中调； Mysql/Redis

IPS_API = DeiviceApiQs(**dict(
    scheme="https://192.168.2.10",
    login_url="/auth/sign",
    logout_url=None,
    user_list_url="/admin/{token}",
    user_info_url="/user/{userid}/{token}",
    login_cfg_url="/user/limit/{token}",
    default_user=['aq009', '999999'],
))
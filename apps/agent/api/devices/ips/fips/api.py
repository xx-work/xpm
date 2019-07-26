from agent.api.devices.ips.settings import prefix, PREFIX_LJ, PREFIX_DL


class ApiINfo(object):
    def __init__(self, url, method='post', name='', desc='', params='', example='', auth=True, response_eg='', data='', _type='c'):
        self.url = url
        self.method = method
        self.name = name
        self.desc = desc
        self.params = params
        self.example = example
        self.auth = auth
        self.response_eg = response_eg
        self.prefix = prefix
        self.data = data
        self._type = _type

    def todict(self):
        return dict(
            url=self.url,
            method=self.method,
            name=self.name,
            desc=self.desc,
            params=self.params,
            example=self.example,
            auth=self.auth,
            response_eg=self.response_eg,
            prefix=self.prefix,
            data=self.data,
            _type=self._type
        )

    def __str__(self):
        return str(self.todict())


IPS_API = [
    ApiINfo(method='post', url='/auth/sign', name='登陆', example='POST /auth/sign username=aq009 password=999999', auth=False, _type='login'),
    ApiINfo(method='post', url=PREFIX_LJ + '/auth/auth', name='鉴权', example='POST /auth/auth sessionid=<>'),
    ApiINfo(method='get',  url=PREFIX_LJ + '/admin/', name='获取所有用户', example='GET /admin'),

    ApiINfo(method='get',    url=PREFIX_LJ + '/user/{pk}/', name='用户信息', desc='获取改用户的信息'),
    ApiINfo(method='put',    url=PREFIX_LJ + '/user/{pk}/', name='修改用户信息', desc='修改用户信息'),
    ApiINfo(method='delete', url=PREFIX_LJ + '/user/{pk}/', name='删除用户'),

    ApiINfo(method='get', url=PREFIX_LJ + '/user/limit/', name='获取用户登陆策略'),
    ApiINfo(method='put', url=PREFIX_LJ + '/user/limit/', name='修改用户登陆策略'),

    ApiINfo(method='get',    url=PREFIX_LJ + '/smtpconf/', name='获取邮件配置'),
    ApiINfo(method='post',   url=PREFIX_LJ + '/smtpconf/', name='修改邮件配置'),
    ApiINfo(method='delete', url=PREFIX_LJ + '/smtpconf/', name='删除邮件配置'),

    ApiINfo(method='get',    url=PREFIX_LJ + '/ipsconf/', name='基于内容的规则'),
    ApiINfo(method='post',   url=PREFIX_LJ + '/ipsconf/', name='添加基于内容的规则'),
    ApiINfo(method='delete', url=PREFIX_LJ + '/ipsconf/', name='删除基于内容的规则'),
    ApiINfo(method='put',    url=PREFIX_LJ + '/ipsconf/', name='批量修改基于内容的规则', params="""[type,[id, code],[id2,code2]]"""),

    ApiINfo(method='get',    url=PREFIX_LJ + '/ruleclass/',  name='获取规则类型列表'),
    ApiINfo(method='get',    url=PREFIX_LJ + '/ipscontrol/', name='查询当前是否有规则未生效'),

    ApiINfo(method='post',   url=PREFIX_LJ + '/ruletplhelper/', name='上传规则模板', params='@upfile'),
    ApiINfo(method='put',    url=PREFIX_LJ + '/ruletplhelper/', name='备份规则模板'),

    ApiINfo(method='get',    url=PREFIX_LJ + '/ruletpls/', name='查询规则模板列表'),
    ApiINfo(method='get',    url=PREFIX_LJ + '/ruletpls/{pk}/', name='获取指定uuid的规则模板'),
    ApiINfo(method='put',    url=PREFIX_LJ + '/ruletpls/{pk}/', name='指定uuid的规则模板修改'),
    ApiINfo(method='delete', url=PREFIX_LJ + '/ruletpls/{pk}/', name='指定uuid的规则模板删除'),

    ApiINfo(method='get',    url=PREFIX_LJ + '/netlog/', name='网络日志'),
    ApiINfo(method='get',    url=PREFIX_LJ + '/bg/sysview/sysinfo/auth/', name='获取授权信息'),
    ApiINfo(method='get',    url=PREFIX_LJ + '/bg/sysview/sysinfo/sys/', name='获取授权信息'),
    ApiINfo(method='get',    url=PREFIX_LJ + '/bg/sysview/netflow/', name='获取流量'),
    ApiINfo(method='get',    url=PREFIX_LJ + '/sysview/engine/', name='获取流量'),

    ApiINfo(method='get',   url=PREFIX_LJ + '/sysview/svrinfo/', name='获取基本系统信息'),
    ApiINfo(method='post',   url=PREFIX_LJ + '/sysview/svrinfo/', name='主机信息', params='methods:[Atck, Flow, Intercept]'),
    ApiINfo(method='post',   url=PREFIX_LJ + '/sysutil/sysop/', name='系统工具', params='methods'),
]
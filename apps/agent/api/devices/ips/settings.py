
prefix = 'https://192.168.2.10'


PREFIX_LJ = '/bg'
PREFIX_DL = '/dl'


IPS_ERROR_RESPONSE = {
    '0': '操作成功',
    '1': '服务器内部错误',
    '2': '参数错误',
    '3': '重复的提交',
    '4': '认证错误,未认证, 或者鉴权失败',
    '5': '登录成功，但没有权限',
    '6': '登录次数限制',
    '50': '操作失败',
}

IPS_DEFAULT_REQUEST_HEADERS = {
   'Accept': 'text/html, application/xhtml+xml, image/jxr, */*',
   'Accept - Encoding': 'gzip, deflate',
   'Accept-Language': 'zh-Hans-CN, zh-Hans; q=0.5',
   'Connection': 'Keep-Alive',
   'X-CSO-Auth': 'f04cf18de880a88d1be3537f0c68dfa1',
   'C-TOKEN-ID': 'iVqFs8jC550jrphTiOu9goEtumxQLNRi',
   'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36 Edge/15.15063'
}

IPS_ROLE_KV = {
    '1': {"alias": "sysuser", "name": "系统管理员"},
    '2': {"alias": "secuser", "name": "安全管理员"},
    '3': {"alias": "audituser", "name": "审计员"},
}

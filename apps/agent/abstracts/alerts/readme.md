# 接口 
```
 http -f POST http://192.168.2.227:18077/cso/agent/pushd_pot_data \
  sig@sig_miguan \
 auth_username=pot001 \
 auth_passwd=112233.. \
 alerts=[]
```

- 单条
```
http -f POST http://192.168.2.227:18077/cso/agent/pushd_sigle_pot_data \
sig@sig_miguan auth_username=pot001 auth_passwd=112233..\
 infosysname=test001 单条接口
```

## 字段说明
```python 
    :param auth_username@str: 连接用户名 pot001
    :param auth_passwd@str: 连接密码 112233..
    :param sig@file: 连接的签名密钥

:param alerts [] 这个数组里面的元素
    :param descover_time: 发现时间
    :param happend_time: 发生时间
    :param infosysname: 告警名称
    :param extra:  额外信息
    :param summary: 告警描述
    :param advice: 告警建议; 计划措施
```

## http://localhost:3322/admin/mgsd/infosecevent/ admin001 112233.. 登陆查看


## 需要使用form_data上传;
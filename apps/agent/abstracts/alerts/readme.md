# 接口 


```
http POST http://192.168.2.227:18077/cso/agent/pushd_pot_data
auth_username=pot001
 auth_passwd=112233.. 
 infosysname=测试-0-0011  
 summary=232123123 
 advice=121321321321 
 extra='fdafdsa'
```

```python 
    :param descover_time: 发现时间
    :param happend_time: 发生时间
    :param infosysname: 告警名称
    :param extra:  额外信息
    :param summary: 告警描述
    :param advice: 告警建议; 计划措施
    :param auth_username: 连接用户名 pot001
    :param auth_passwd: 连接密码 112233..
```

## http://localhost:3322/admin/mgsd/infosecevent/ admin001 112233.. 登陆查看
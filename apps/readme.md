# 2019-6-19
- 1, 修改具体的策略指向的具体内容，优化表格的设计。
- 2, 修改部分关于监控的内容，策略，审计。


# 具体任务


## 2019-6-19
- 1, 需要修改chk/audit变更和审计的用户名的存储，以及审计事件添加的表格。
- 2, 需要增加和完善处理逻辑, 修改对应的接入客户端的脚本。
- 3, 平台提供客户端接入的URL, 加密和解密传入数据即可。
- 4, 客户端的运行, 依赖于服务端传给过去的字段预先记录。

**NOTE**
- 1, 之所以审计和变更操作都用字符串, 而不是真正的对象，防止用户删除后，对应用户的操作内容丢失。
- 2, 数据表格, 平台数据备份和恢复。使用mysql-server备份和目录挂载。

## 2019-6-20
- 完善视图和基本的数据填充;
- 整理服务端开放接口; 让客户端进行请求的过程中发送

## 2019-6-22 
- 完成了系统部件的识别和主要进程监控
  - 这里的主要进程是用户管理进程正常。
- 完成了部分前端界面的内容。
- 变更逻辑也正在完善。目前仍然在整理安全机制策略。其他的都已完成。

## 2019-6-24
- 1, 修改部分关于
- 2, requsets请求API和反馈自定义抢球头和传递参数，
- 3. SNMP负载减小。


## 2019-6-25
- 去掉花里胡哨的CSO管理
 - `../../cso_venv/bin/celery worker -A ops -l INFO --autoscale=20,4 --detach --logfile=../logs/celery-worker.log`
 - `../../cso_venv/bin/celery -A ops beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler --max-interval=60 --detach --logfile=../logs/celery-beat.log`
 - `../../cso_venv/bin/flower --address=0.0.0.0 --port=5555 --broker=redis://:xxscan@192.168.2.227:6379/3 --log-to-stderr=../logs/flower.log --persistent`
 - `../../cso_venv/bin/gunicorn website.wsgi -b 0.0.0.0:8888 -w 2 -p /home/django/xpm/tmp/gunicorn.pid --access-logformat %(h)s %(t)s "%(r)s" %(s)s %(b)s  --error-logfile ../logs/gunicorn.log --log-level DEBUG --access-logfile /var/log/hop_srv_access.log`
- 修改目录结构
 - 替换原来的`server`为当前的 `manager`
 - 用`pycharm`替换`service`为 `secs`记录平台的安全机制。
    - `services/oauth`
    - `services/platlog` 
    - 其他常见工具
 

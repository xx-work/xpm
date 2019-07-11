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
 - `celery worker -A ops -l INFO --autoscale=20,4 --detach --logfile=/opt/celery-worker.log`
 - `celery -A ops beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler --max-interval=60 --detach --logfile=/opt/celery-beat.log`
 - `flower --address=0.0.0.0 --port=5555 --broker=redis://:xxscan@192.168.2.227:6379/3 --log-to-stderr=../logs/flower.log --persistent`
 - `gunicorn website.wsgi -b 0.0.0.0:8888 -w 2 -p /home/django/xpm/tmp/gunicorn.pid --access-logformat %(h)s %(t)s "%(r)s" %(s)s %(b)s  --error-logfile ../logs/gunicorn.log --log-level DEBUG --access-logfile /var/log/hop_srv_access.log`
- 修改目录结构
 - 替换原来的`server`为当前的 `manager`
 - 用`pycharm`替换`service`为 `secs`记录平台的安全机制。
    - `services/oauth`
    - `services/platlog` 
    - 其他常见工具
 
 
## 2019-6-26
- 注意事项, 1审计对象, 2安全机制。
- 全部改写 Xadmin 跟测试文档一样。

## 2019-7-2
- 补充很多结构, 存在重大的问题。很多内容都没有细化到具体的进程。
- 注意: 一旦要重写首页抛弃原来的首页结构，使用中间件强制跳转即可。
- [github表情](https://www.jianshu.com/p/bb26733da917)

## 2017-7-3 
- 结构更改和全局使用的设置。
- 全部结构使用。
- 修改这个核心结构为 mgsd `manager-server-d` 

## 2019-7-8
- 1, 需要增加组织批准接入的接口
- 2, 需要增加执行策略的内容; 同步时间/在线升级/修改配置等。
- 3, 需要修改对应的监控的指标内容和响应。

## 2019-7-9
- 1, 开始捕获对象变更和变更进入审计的流程; 主要是对象变更和接入，策略变更等。
- 2, 今天先完成对象变更的内容，关于策略录入和策略下发等，明天再弄。
  - 步骤: 首选进行对象变更和接入。统计所有Log里面关于对象变更的内容; 取出来需要的内容进行过滤。
  - 步骤: 接着增加一列, 是否手动修改进入响应处置。
  
## 2019-7-10 
- 1, 修改数据库为新的数据库，进行审计和处理后续的内容

```
 ConnectManagerUserInfo.objects.create(name='非特权系统管理用户', \
 username='admin001', _password='11fd32234Q42q==')
```
## 2019-7-11
- 今天出现了权限异常的问题; 无法一对一的获取。permission_group 视图。
- 仍然没有解决的问题是策略管理的优化。
- [git表情大全](https://github.com/liuchengxu/git-commit-emoji-cn)

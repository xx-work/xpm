## 2019-5-16
- 1,完成了系统部件监控的部分监控数据内容字段的编写和信息收集。
  - 当前主要是填充数据和需要的表字段填充。
  - 监控数据的内容后面需要继续完善
- 2,完成了系统部件管理, 增删改识别系统部件的逻辑和审计。
  - 识别自己的设备, 统计和管理增加的设备。
- 3,完成了一些关于系统部件策略的基本逻辑.
  - 主要是策略基准和策略规则, 绑定用户组, 正在完善。
  - 策略下发,策略完整性相关的逻辑完善。
- 4, 完成了处置监督、应急预案报告的内容表格创建。
  - 处置监督应急预案的模板建立和对应事件类别(部件审计, 攻击, 平台变更)进行细致分类
- 5, 完成了备份和灾难备份的任务推进。
- 6, 下一步需要进行完善的。
  - 1, 任务审计。系统部件监控、规则变更、平台变更操作的审计(记录成功与否以及原因)
  - 2, 平台执行审计的任务情况统计。
  - 3, 信息收集和相关部件策略下发逻辑完善。
 

## 2019-5-20
- `982a46afb81aa2bcbca7c59780c31a9dede88c0c` 

## 2019-5-21
- 当前系统部件的信息都是手动填写; 并没有通过队列推送的形式自动获取
- 后期如果要自动获取设备的硬件信息可以通过 


## 2019-5-22
- https://gitee.com/meigea/ACLight/raw/master/LICENSE
- 统计当前代码中使用的工具


- Web中间件 [Nginx/Tengine](https://github.com/alibaba/tengine)
- WAF引擎 [ModSecurity](https://github.com/SpiderLabs/ModSecurity)
- 日志收集 [Fluentd](https://github.com/fluent/fluentd)
- Web开发框架 [Python-Django](https://github.com/django/django)
- 任务调度框架 [Celery](http://docs.celeryproject.org/en/latest/)
- 数据库 Redis Mongodb Mysql Sqllite

## 2019-5-28
- 1, 完全规划完毕系统策略的内容
- 2, 信息收集的定时任务完成
- 3, 系统策略的预备处理[0]
- 4, 系统备份逻辑的完善。ORM创建。
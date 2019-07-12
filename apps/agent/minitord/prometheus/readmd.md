# prometheus 作为客户端使用

- [中文入门指南](https://www.ibm.com/developerworks/cn/cloud/library/cl-lo-prometheus-getting-started-and-practice/)
- [prometheus一套服务](https://www.cnblogs.com/chenqionghe/p/10494868.html)


## 简要介绍组件和功能
- [基本介绍](https://mp.weixin.qq.com/s/tO1dzAHBc553QI3qaSXNFQ)
- [安装和指标说明](https://mp.weixin.qq.com/s/m9GNwhJQjkFjhd3RnBAJ4Q)
- [架构](https://mp.weixin.qq.com/s/TK5nsRdohOvSOmxRGEn0ig)
- [prometheus+Grafana](https://blog.51cto.com/itstyle/1980064)
- [踩坑1](https://mp.weixin.qq.com/s/8AqQPZfG_plMKivpblylhg)
- [Zabix4.2+prom自动发现](https://mp.weixin.qq.com/s/nyRMKPC2y4p89BsHtkWBEg)

![架构图](../../static/agent/imgs/image001.png)

> Prometheus生态系统由多个组件组成，它们中的一些是可选的。多数Prometheus组件是Go语言写的，这使得这些组件很容易编译和部署。

### Prometheus Server 
> 主要负责数据采集和存储，提供PromQL查询语言的支持。

### 客户端SDK 
> 官方提供的客户端类库有go、java、scala、python、ruby，其他还有很多第三方开发的类库，支持nodejs、php、erlang等。

### Push Gateway
> 支持临时性Job主动推送指标的中间网关。

### PromDash
> 使用Rails开发可视化的Dashboard，用于可视化指标数据。

### Exporter
> Exporter是Prometheus的一类数据采集组件的总称。它负责从目标处搜集数据，并将其转化为Prometheus支持的格式。与传统的数据采集组件不同的是，它并不向中央服务器发送数据，而是等待中央服务器主动前来抓取。

### alertmanager
> 警告管理器，用来进行报警。

### prometheus_cli
> 命令行工具。

### 其他辅助性工具
> 多种导出工具，可以支持Prometheus存储数据转化为HAProxy、StatsD、Graphite等工具所需要的数据存储格式。

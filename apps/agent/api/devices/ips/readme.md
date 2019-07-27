# 目录说明和基本功能介绍

- in 代表的是管理部件IPS和CSO平台通信过程中主动进行发送的机制。/ 主要是处理IPS的接口和接收
- out 代表的是CSO将自身对于管理部件的一些信息传导给IPS


# 重点-逻辑修改和对接
- inital_api 记录的是 IPS_API
- settings 记录的是接口的示例需要修改的 /bg
- fips/ 记录的是 from-ips 获取的接口的API
- [核心的requests处理文件 `intercepter.py`](../../devices/ips/fips/intercepter.py)
- [测试脚本文件](../../../../mgsd/xint/2019_07_24_inital_ips_respose-v2.py)
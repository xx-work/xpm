# 审计相关的脚本

- 可以基于HTTP-Agent也可以基于自定义的SNMP脚本; 两种弄法。
- 通过SNMP脚本获取的话。


## 普通服务器监控，进程或者软件安全情况。
- [SNMP安全配置](https://www.cnblogs.com/yangykaifa/p/7135730.html)


## 设置2;
- 1, 监控日志系统是否运行。
- 2, 监控各种机制是否正常。


```bash
docker run \
-d \
--name snmpd \
--net=host \
-v ./snmpd.conf:/etc/snmpd/snmpd.conf \
polinux/snmpd:alpine \
-c /etc/snmpd/snmod.conf
```

### snmpd.conf
- 默认文件下 `cat /etc/snmp/snmpd.conf | grep -v '#' | grep -v ^$`
- 接着修改成自己想要的组

```
com2sec notConfigUser  default       public

group   notConfigGroup v1           notConfigUser
group   notConfigGroup v2c           notConfigUser

view    systemview    included   .1.3.6.1.2.1.1
view    systemview    included   .1.3.6.1.2.1.25.1.1

access  notConfigGroup ""      any       noauth    exact  all none none

com2sec local     localhost       COMMUNITY
com2sec mynetwork NETWORK/24      COMMUNITY

group MyRWGroup  any        local
group MyROGroup  any        mynetwork
group MyRWGroup  any        otherv3user

view all    included  .1                               80
view mib2   included  .iso.org.dod.internet.mgmt.mib-2 fc

access MyROGroup ""      any       noauth    0      all    none   none
access MyRWGroup ""      any       noauth    0      all    all    all
access notConfigGroup "" any       noauth    0      all    all    all

com2sec notConfigUser   default         public
group   notConfigGroup  v1              notConfigUser
group   notConfigGroup  v2c             notConfigUser

view    roview          included        .1
view    rwview          included        system.sysContact
view    rwview          included        system.sysName
view    rwview          included        system.sysLocation
view    rwview          included        interfaces.ifTable.ifEntry.ifAdminStatus
view    rwview          included        at.atTable.atEntry.atPhysAddress
view    rwview          included        at.atTable.atEntry.atNetAddress
view    rwview          included        ip.ipForwarding
view    rwview          included        ip.ipDefaultTTL
view    rwview          included        ip.ipRouteTable.ipRouteEntry.ipRouteDest
view    rwview          included        ip.ipRouteTable.ipRouteEntry.ipRouteIfIndex
view    rwview          included        ip.ipRouteTable.ipRouteEntry.ipRouteMetric1
view    rwview          included        ip.ipRouteTable.ipRouteEntry.ipRouteMetric2
view    rwview          included        ip.ipRouteTable.ipRouteEntry.ipRouteMetric3
view    rwview          included        ip.ipRouteTable.ipRouteEntry.ipRouteMetric4
view    rwview          included        ip.ipRouteTable.ipRouteEntry.ipRouteType
view    rwview          included        ip.ipRouteTable.ipRouteEntry.ipRouteAge
view    rwview          included        ip.ipRouteTable.ipRouteEntry.ipRouteMask
view    rwview          included        ip.ipRouteTable.ipRouteEntry.ipRouteMetric5
view    rwview          included        ip.ipNetToMediaTable.ipNetToMediaEntry.ipNetToMediaIfIndex
view    rwview          included        ip.ipNetToMediaTable.ipNetToMediaEntry.ipNetToMediaPhysAddress
view    rwview          included        ip.ipNetToMediaTable.ipNetToMediaEntry.ipNetToMediaNetAddress
view    rwview          included        ip.ipNetToMediaTable.ipNetToMediaEntry.ipNetToMediaType
view    rwview          included        tcp.tcpConnTable.tcpConnEntry.tcpConnState
view    rwview          included        egp.egpNeighTable.egpNeighEntry.egpNeighEventTrigger
view    rwview          included        snmp.snmpEnableAuthenTraps

access  notConfigGroup ""      any       noauth    exact  roview rwview none

syslocation Unknown (edit /etc/snmp/snmpd.conf)
syscontact Root <root@localhost> (configure /etc/snmp/snmp.local.conf)
dontLogTCPWrappersConnects yes
disk / 36805060
load 12 14 14
exec .1.3.6.1.4.1.2021.50 /bin/echo helloword
exec .1.3.6.1.4.1.2021.51 ps /bin/ps
exec .1.3.6.1.4.1.2021.52 top /usr/local/bin/top
pass .1.3.6.1.4.1.2021.255 /bin/echo hello-zcs

rwcommunity sysinfo

#extend mem1 /bin/bash /home/snmp/cmds/mem.sh
#extend cpu1 /bin/bash /home/snmp/cmds/cpu.sh
#extend net_eth0 /bin/bash /home/snmp/cmds/net.sh
```
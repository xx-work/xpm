# PySnmp 脚本调用
- pysnmp==4.4.9



## 2019-5-22
- 1, 当前不考虑v3


## 2019-7-17
- 1. 放下prometheus重新弄snmp
- [net-snmp](http://www.net-snmp.org)



## 基本命令
```bash
snmpwalk -v 2c -c cyasnmpv2 192.168.2.227 IP-MIB::ipAdEntAddr
snmpwalk -v 2c -c cyasnmpv2 192.168.2.227 1.3.6.1.2.1.25.4.2.1.2
```
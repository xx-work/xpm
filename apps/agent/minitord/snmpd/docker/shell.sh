#!/usr/bin/env bash

yum -y install gcc make perl perl-devel file ;
wget https://nchc.dl.sourceforge.net/project/net-snmp/net-snmp/5.8/net-snmp-5.8.tar.gz && \
tar zxvf net-snmp-5.8.tar.gz && \
cd net-snmp-5.8 && \
./configure --prefix=/snmpd --build=x86_64-linux  \
--enable-mfd-rewrites \
--with-default-snmp-version=2 \
--with-sys-contact=admin@gzqinglang.com \
--with-sys-location=China \
--with-logfile=/snmpd/var/snmpd.log \
--with-persistent-directory=/snmpd/var/net-snmp && make && make install && cp EXAMPLE.conf /snmpd/snmpd.conf && rm -rf ../net-snmp-5.8*

/smmpd/sbin/smmpd -f -c -C /snmpd/snmpd.conf

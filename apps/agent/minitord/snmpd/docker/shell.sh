#!/usr/bin/env bash

yum -y install gcc make perl perl-devel file



wget https://nchc.dl.sourceforge.net/project/net-snmp/net-snmp/5.8/net-snmp-5.8.tar.gz && \
tar zxvf net-snmp-5.8.tar.gz && \
cd net-snmp-5.8 && \
./configure --prefix=/software/net-snmp \
--enable-mfd-rewrites \
--with-default-snmp-version=2 \
--with-sys-contact=admin@gzqinglang.com \
--with-sys-location=China \
--with-logfile=/var/log/snmpd.log \
--with-persistent-directory=/var/net-snmp && make && make install
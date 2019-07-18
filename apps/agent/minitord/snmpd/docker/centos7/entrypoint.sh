#!/bin/bash

if [ ${SNMP_MODE}='agent' ]; then
    ${INSTALL_PATH}/sbin/snmpd -C -c /etc/snmpd.conf;
else
    ${INSTALL_PATH}/sbin/snmpd -C /etc/snmpd.conf;
    # /usr/bin/snmptrap -C /software/net-snmp/snmptrap.conf;
fi

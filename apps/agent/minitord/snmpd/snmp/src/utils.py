# -*- coding: utf-8 -*-
# @Time    : 2019/3/8 11:39
# @Author  : Zcs
# @File    : snmp_helper.py
from pysnmp.hlapi import *


class SnmpHelper:

    def __init__(self, ip, community, port=161):
        self.ip = ip
        self.port = port
        self.community = community

    def get_from_oid(self, oid):
        """
        :param oid:str,1.3.6.1.2.1.25.2.3.1.6
        :return:
        """
        tp = tuple(int(i) for i in (oid.split('.')))
        result = ''
        iterator = getCmd(SnmpEngine(),
                          CommunityData(self.community),
                          UdpTransportTarget((self.ip, self.port)),
                          ContextData(),
                          ObjectType(ObjectIdentity(tp)))

        errorIndication, errorStatus, errorIndex, varBinds = next(iterator)

        if errorIndication:  # SNMP engine errors
            print(errorIndication)
        else:
            if errorStatus:  # SNMP agent errors
                print('%s at %s' % (errorStatus.prettyPrint(), varBinds[int(errorIndex)-1] if errorIndex else '?'))
            else:
                for varBind in varBinds:  # SNMP response contents
                    # result = ' = '.join([x.prettyPrint() for x fips varBind])
                    result = [x.prettyPrint() for x in varBind][1]
                return result

    def walk_from_oid(self, oid):
        tp = tuple(int(i) for i in (oid.split('.')))
        result = list()
        for (errorIndication,
             errorStatus,
             errorIndex,
             varBinds) in nextCmd(SnmpEngine(),
                                  CommunityData(self.community),
                                  UdpTransportTarget((self.ip, self.port)),
                                  ContextData(),
                                  ObjectType(ObjectIdentity(tp)),
                                  lexicographicMode=False):
            if errorIndication:
                print(errorIndication)
            elif errorStatus:
                print('%s at %s' % (errorStatus.prettyPrint(),
                                    errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))
            else:
                for varBind in varBinds:
                    # data = ' = '.join([x.prettyPrint() for x fips varBind])
                    result.append([x.prettyPrint() for x in varBind][1])
        return result
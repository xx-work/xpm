from .conf import config_template
from .utils import SnmpHelper

oid_dict = config_template['SNMP_OID']


class DevSnmpHandler():

    def __init__(self, ip='192.168.2.41', port=161, community="sysinfo"):
        """
        SNMP-V2调用
        :param ip:
        :param port:
        :param community:
        """
        self.ip = ip
        self.port = port
        self.community = community

    def conn_agent(self):
        snmp_helper = SnmpHelper(ip=self.ip, community=self.community, port=self.port)
        return snmp_helper

    def get_current_flow(self):
        snmp_helper = self.conn_agent()
        recv_data = snmp_helper.walk_from_oid(oid_dict['if_recv_flow']['oid'])
        send_data = snmp_helper.walk_from_oid(oid_dict['if_send_flow']['oid'])
        recv_flow = sum(int(i) for i in recv_data)
        send_flow = sum(int(i) for i in send_data)
        return send_flow, recv_flow

    def get_current_process(self):
        snmp_helper = self.conn_agent()
        process_list = snmp_helper.walk_from_oid(oid_dict['sys_run_process']['oid'])
        return process_list

    def get_current_software(self):
        snmp_helper = self.conn_agent()
        software_list = snmp_helper.walk_from_oid(oid_dict['sys_software']['oid'])
        return software_list

    def get_up_time(self):
        snmp_helper = self.conn_agent()
        up_time = snmp_helper.get_from_oid(oid_dict['sys_up_time']['oid'])
        return up_time

    def get_percent_data(self):
        snmp_helper = self.conn_agent()
        cpu_data = round(float(snmp_helper.get_from_oid(oid_dict['cpu_percent']['oid'])), 2)
        cpu_percent = cpu_data if cpu_data > 0 else 0.1
        disk_data = round(float(snmp_helper.walk_from_oid(oid_dict['disk_percent']['oid'])[0]), 2)
        disk_percent = disk_data if disk_data > 0 else 0.1
        used_mem = int(snmp_helper.get_from_oid(oid_dict['real_mem_used']['oid']))
        total_mem = int(snmp_helper.get_from_oid(oid_dict['real_mem_total']['oid']))
        mem_percent = round(used_mem / total_mem, 2)
        return cpu_percent, mem_percent, disk_percent
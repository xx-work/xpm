import os, sys, django

def start_django():
    DjangoModulePath = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(DjangoModulePath)
    os.chdir(DjangoModulePath)
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "website.settings")
    django.setup()



def main():
    start_django()
    from cso.mudules.monitor.nmap_tool.get_nmap_datas import get_needs_datas_from_xmlpath

    get_needs_datas_from_xmlpath(xml_path="F:\\workspace\\CSO\\aa.xml")

def test2():
    import subprocess
    p = subprocess.Popen("ls -alh", shell=True)
    print(p.pid)

    import os
    os.waitpid(p.pid, os.W_OK)

def test_snmp():
    start_django()

    from cso.mudules.monitor.snmp.src.dev import DevSnmpHandler

    print(DevSnmpHandler().get_current_flow())
    print(DevSnmpHandler().get_current_process())
    print(DevSnmpHandler().get_percent_data())
    print(DevSnmpHandler().get_current_software())
    print(DevSnmpHandler().get_up_time())

def test_snmp2():
    start_django()

    from cso.mudules.monitor.snmp.inital import inital_data
    inital_data()

def test_snmp3():
    start_django()

    from cso.mudules.monitor.snmp.collect import collect_datas
    collect_datas()


if __name__ == '__main__':
    #main()
    #test_snmp()
    # test_snmp2()
    # test_snmp3()

    main()




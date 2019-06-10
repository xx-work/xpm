import os
import uuid

from website.settings import PROJECT_DIR
NmapDataDir = os.path.join(PROJECT_DIR, "nmap_datas")
if not os.path.exists(NmapDataDir):
    os.mkdir(NmapDataDir)

Nmap_xml_result_path = os.path.join(NmapDataDir, "nmap_result_" + str(uuid.uuid4()) + ".xml")

NmapScanDefaultBin = "/usr/bin/nmap"
NmapScanDefaultArgs = "-sS -sV -p1-65535 -O"
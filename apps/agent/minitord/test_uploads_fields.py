import requests
import json

sig_file = "C:\\Users\\admin001\\Downloads\\sig_miguan"


def push_pot_alerts(alerts_data2):
    url = "http://192.168.2.227:18077/cso/agent/pushd_pot_data"
    files = {'sig': ('sig_file', open(sig_file, 'rb'), 'application/octet-stream', {'Expires': '0'})}
    r = requests.post(url, files=files, data={
        "auth_username": "pot001",
        "auth_passwd": "112233..",
        "alerts": json.dumps({"data": alerts_data2})
    })
    print(r.text)


if __name__ == '__main__':
    alerts_data2 = [
        {"infosysname": "SSH暴力破解尝试", "advice": "使用fail2ban工具进行过滤。", "summary": "频繁多用户密码连接22端口", "extra": "01",
         "happend_time": "2019-7-12 11:12:11", "descover_time": "2019-7-12 11:13:11"},
        {"infosysname": "WEB目录URL暴力破解尝试", "advice": "使用fail2ban工具进行过滤。或者开启WAF", "summary": "目录遍历，疑似发现敏感URL进行攻击.", "extra": "02",
         "happend_time": "2019-7-13 11:12:11", "descover_time": "2019-7-13 11:13:11"},
    ]

    push_pot_alerts(alerts_data2)
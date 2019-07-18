import requests

request_lines = """


Host: report.rich-healthcare.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2
Accept-Encoding: gzip, deflate, br
Referer: https://report.rich-healthcare.com/medicalReport/app/loginController/checkLogin
Content-Type: application/x-www-form-urlencoded
Content-Length: 73
Connection: keep-alive
Upgrade-Insecure-Requests: 1

"""


import re


def matched_header_line(headers, header_line):
    matched = re.match("([\w_\-]+)\: (.*)", header_line)
    if matched:
        headers[matched.group(1)] = matched.group(2)
    return headers


def get_cookie():
    headers = {}
    for x in request_lines.split('\n'):
        headers = matched_header_line(headers, x)
    session = requests.session()
    session.headers = headers
    response = session.post(url="https://report.rich-healthcare.com/medicalReport/app/loginController/checkLogin",
                           data=dict(loginWay=2, countDownTime='', username='952100624322', password='89A254', x=45, y=22),
                           allow_redirects=False)

    reffer = response.request.headers
    print(reffer)


def replace_cookie(cookie):
    with open('/etc/nginx/conf.d/80.conf', "r+", encoding='utf-8') as f:
        strs = f.read()
        f.close()
    with open('/etc/nginx/conf.d/80.conf', "w+", encoding='utf-8') as f:
        ws = """"""
        for line in strs.split("\n"):
            if re.match("(.*?)proxy_set_header Cookie.*?", line):
                ws += re.match("(.*?)proxy_set_header Cookie.*?", line).group(1) + """proxy_set_header Cookie "{}";\n""".format(cookie)
                continue
            ws += line + "\n"
        f.write(ws)
    print("复位cookie成功")


if __name__ == '__main__':
    cookie = get_cookie()
    print("新产生了cookie")
    print(cookie)
    try:
        replace_cookie(cookie)
    except:
        print('替换失败')

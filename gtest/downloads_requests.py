import requests
import re
from io import BytesIO


def usets():
    with open("./data.txt", "r+", encoding='utf-8') as f:
        strings = f.read()
        f.close()
    partern = ".*?Downloading (https://mirrors.tuna.tsinghua.edu.cn/pypi/web/packages/.*?) .*?"
    datas = re.findall(partern, strings)
    return list(datas)


def downloads_bytes(url):
    r = requests.get(url, stream=True)
    chunk_size = 10240
    with open(url.split("/")[-1], 'wb') as fd:
        for chunk in r.iter_content(chunk_size):
            fd.write(chunk)
    print(url)


if __name__ == '__main__':
    for url in usets():
        downloads_bytes(url)

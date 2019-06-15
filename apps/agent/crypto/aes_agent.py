# coding:utf-8

import base64
import json


from Cryptodome.Cipher import AES
AES_ENCODE_KEY = "1q2w3e4R" * 4


# 补足字符串长度为16的倍数
def add_to_16(s):
    while len(s) % 16 != 0:
        s += '\0'
    return str.encode(s)  # 返回bytes

def encrypted(text, key=AES_ENCODE_KEY):
    aes = AES.new(str.encode(key), AES.MODE_ECB)  # 初始化加密器，本例采用ECB加密模式
    return str(base64.encodebytes(aes.encrypt(add_to_16(text))), encoding='utf8').replace('\n', '')  # 加密


def decriptd(encrypted_text, key=AES_ENCODE_KEY):
    aes = AES.new(str.encode(key), AES.MODE_ECB)  # 初始化加密器，本例采用ECB加密模式
    return str(aes.decrypt(base64.decodebytes(bytes(encrypted_text, encoding='utf8'))).rstrip(b'\0').decode("utf8"))  # 解密

def encoded_json(obj, key=AES_ENCODE_KEY):
    text = json.dumps(obj) ## 将加密的json对象转化为字符串。
    return encrypted(text, key=key)


def decoded_json(encode_s, key=AES_ENCODE_KEY):
    results = json.loads(decriptd(encode_s, key=key))
    return results


def test_encode_and_decode_json(json_dcit):
    s_encode = encoded_json(json_dcit, key=AES_ENCODE_KEY)
    print(s_encode)
    d_decode = decoded_json(s_encode)
    print("解密后：")
    print(d_decode)
    print(type(d_decode))


if __name__ == '__main__':
    test_encode_and_decode_json({"a": [i for i in range(100)]})
    test_encode_and_decode_json({"a": [i for i in range(600)]})
    test_encode_and_decode_json({"a": [i for i in range(700)]})



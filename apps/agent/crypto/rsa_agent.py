# coding:utf-8

## https://stuvel.eu/python-rsa-doc/usage.html#generating-keys
import rsa


(bob_pub, bob_priv) = rsa.newkeys(4096)


def encoded_text(s, public_key=bob_pub):
    s_encoded = rsa.encrypt(s.encode('utf-8'), public_key)
    return s_encoded


def decoded_text(s_encoded, primary_key=bob_priv):
    s_decoded = rsa.decrypt(s_encoded, primary_key)
    return s_decoded


def test():
    d = {}
    d["a"] = 2
    d["b"] = 3
    d["c"] = [i for i in range(11)]

    import json
    text = json.dumps(d)
    print(text)

    en = encoded_text(text)
    de = decoded_text(en)
    print(en)
    print(de)

    results = json.loads(de)

    print(results)


if __name__ == '__main__':
    test()
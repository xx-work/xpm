import rsa
from src import django_setup
django_setup()

from agent.api.devices.pot.alerts import load_cop_user
user = load_cop_user()

IV = '1q2w3e4R'.encode('UTF-8')


SIG_MIGUANF_FILE = 'agent/crypto/datas/sig_miguan'


def load_sig_from_file_and_jg(public, file_name=SIG_MIGUANF_FILE, IV=IV):
    with open(file_name, 'rb') as f:
        sig = f.read()
        f.close()
    try:
        slug = rsa.verify(IV, sig, public)
        return slug == 'SHA-1'
    except:
        return False


def load_true_sig(private_key, file=SIG_MIGUANF_FILE):
    exec('priv_key = {}'.format(private_key))
    sig = rsa.sign(IV, locals()['priv_key'], 'SHA-1')
    try:
        return sig
    finally:
        with open(file, 'wb') as f:
            f.write(sig)
            f.close()
        return True


def load_sig_from_file(file=SIG_MIGUANF_FILE):
    with open(file, 'rb') as f:
        sig = f.read()
        f.close()
    return sig


def user_sig_is_ture(_public_key, sig, IV=IV):
    exec('public = {}'.format(_public_key))
    try:
        slug = rsa.verify(message=IV, signature=sig, pub_key=locals()['public'])
        return slug=='SHA-1'
    except:
        return False


if __name__ == '__main__':
    print(user_sig_is_ture( user._public_key, sig=load_sig_from_file()))

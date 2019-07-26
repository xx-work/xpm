import rsa
from src import django_setup
django_setup()


def main():
    from agent.api.devices.ips.inital_api import push_ips_apis
    push_ips_apis()


if __name__ == '__main__':
    main()

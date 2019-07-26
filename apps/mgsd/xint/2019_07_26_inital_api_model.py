import rsa
from src import django_setup
django_setup()


def main():
    from agent.api.interceptors.request_ips import IpsRequestMiddleHandle
    from agent.api.devices.agent_api import IPS_API

    from agent.api.devices.models import AgentApi
    from agent.api.devices.ips.fips.api import ApiINfo



if __name__ == '__main__':
    main()

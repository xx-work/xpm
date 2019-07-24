def test_perm():
    from src import django_setup

    django_setup()
    from datetime import datetime
    _now = datetime.now()
    from agent.api.devices.pot.alerts import pot2cso
    data = pot2cso(descover_time=_now, happend_time=_now,
            infosysname='test1', extra='', summary='', advice='')
    print(data)


if __name__ == '__main__':
    test_perm()
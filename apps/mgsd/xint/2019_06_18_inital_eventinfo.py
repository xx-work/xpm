from src import django_setup


def inintal_eventtypes():
    django_setup()
    import logging

    from mgsd.models import EffectInfo, AttackerActionDesc

    try:

        EffectInfo.inital()
        AttackerActionDesc.inital()

        logging.info("初始化时间机制成功")
        print("初始化时间机制成功")
    except:
        logging.error("初始化事件失败")
        print("初始化事件失败")


if __name__ == '__main__':
    inintal_eventtypes()



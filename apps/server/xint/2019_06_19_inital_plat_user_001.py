from src import django_setup


def createuser(username, password):
    django_setup()
    import logging
    from django.contrib.auth.models import User
    try:
        user = User.objects.create_superuser(username=username, password=password, email='test@example.com')
        user.is_staff = True
        user.save()
        logging.info("创建用户成功")
        print("创建用户成功")
    except:
        pass


if __name__ == '__main__':
    createuser(username='admin001', password='112233..')


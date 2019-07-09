


if __name__ == '__main__':
    from src import django_setup

    django_setup()

    from mgsd.api.solution.models import PolicyBaseTypes, InfoSecEventTypes, InfoSecEvent
    InfoSecEvent.objects.filter(info_type=InfoSecEventTypes[1][0]).delete()

    from mgsd.xtool.log2solution import demo_user_render, demo_cop_render, demo_audit_render

    demo_user_render()
    demo_cop_render()
    demo_audit_render()
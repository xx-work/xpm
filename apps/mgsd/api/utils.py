from django.utils.decorators import method_decorator, classonlymethod
from django.utils.encoding import force_text, smart_text, smart_str
from django.views.decorators.csrf import csrf_protect
csrf_protect_m = method_decorator(csrf_protect)

from mgsd.api.chk.log.models import Log


def get_content_type_for_model(obj):
    from django.contrib.contenttypes.models import ContentType
    return ContentType.objects.get_for_model(obj, for_concrete_model=False)


def log(flag, user, request, message, obj=None):
    log = Log(
        user=user,
        ip_addr=request.META['REMOTE_ADDR'],
        action_flag=flag,
        message=message
    )
    if obj:
        log.content_type = get_content_type_for_model(obj)
        log.object_id = obj.pk
        log.object_repr = force_text(obj)
    log.save()
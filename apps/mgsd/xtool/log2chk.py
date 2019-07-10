from xadmin.models import Log

# from django.contrib.contenttypes.models import ContentType
from mgsd.api.chk.models import PolicyBaseTypes


def get_category_of_models_by_modelname(app_name):
    """

    :param app_name: app_name 下所有的
    :return:
    """

    return


AUDIT_CHK_KV = {
    PolicyBaseTypes[0][0]: ['sysmanagercopinfo', 'objprocess', ],
    PolicyBaseTypes[1][0]: ['connectmanageruserinfo', ],
    PolicyBaseTypes[2][0]: ['auditlogobject', ],
}


def get_chk_recode_by_log(type='security'):
    qs = Log.objects.filter(content_type__app_label__in=('mgsd', ), content_type__model__in=AUDIT_CHK_KV[type])
    return qs



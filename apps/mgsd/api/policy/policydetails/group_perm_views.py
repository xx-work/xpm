# coding:utf-8

from django.contrib.auth.models import Group, Permission, ContentType
from django.forms.models import model_to_dict
from django.utils.translation import ugettext as _


def _local_trans(string):
    return string.replace('Can ',  '能够').replace('view ', '查看').replace('change ',
                                '修改').replace('delete ', '删除').replace('add ', '增加')


def get_group_perm_view_table(_group=Group.objects.all()[0]):
    """
    获取对应组下group_view的表。
    :param group_id: group的id
    :return:
    """
    # from django.contrib.auth.models import Group, Permission, ContentType

    moudle_preform = lambda module_str, module_name, lables: """<fieldset id="module_{module_str}">
            <legend>{module_name}</legend>{lables}</fieldset>""".format(module_name=_local_trans(module_name), module_str=module_str,
                                                                        lables=lables)
    _lable_html = lambda checked, perm_id, perm_name: """<label class="floating">
                <input type="checkbox" name="role[permissions][]" id="role_permissions_{perm_id}" value="view_changesets" data-shows=".view_changesets_shown" {checked}>
                {perm_name}
                </label>""".format(perm_id=perm_id, perm_name=_local_trans(perm_name), checked='checked="checked"' if checked else '')

    content_types = ContentType.objects.all()
    permitions = Permission.objects.all()
    _perms = _group.permissions.all()
    _registerd_ctypes = [x.content_type for x in _perms]

    _all_strs = """"""
    for ctype in content_types:
        if ctype in _registerd_ctypes:
            _p = _perms.filter(content_type=ctype)
            p = permitions.filter(content_type=ctype)
            labels = """"""
            for x in p:
                _checkd = x in _p
                labels += _lable_html(perm_id=x.codename, perm_name=str(x.name), checked=_checkd)
            mudule_str = moudle_preform(module_str=ctype.id, module_name=ctype.name.replace('Can ', '能够'), lables=labels)
            _all_strs += mudule_str

    return _all_strs
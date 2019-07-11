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

    moudle_preform = lambda module_str, module_name, lables: """<br><fieldset id="module_{module_str}">
            <legend>{module_name}</legend>{lables}</fieldset>""".format(module_name=_local_trans(module_name), module_str=module_str,
                                                                        lables=lables)
    _lable_html = lambda checked, perm_id, perm_name: """<label class="floating">
                <input type="checkbox" name="role[permissions][]" id="role_permissions_{perm_id}" value="view_changesets" data-shows=".view_changesets_shown" {checked}>
                {perm_name}
                </label>""".format(perm_id=perm_id, perm_name=_local_trans(perm_name), checked='checked="checked"' if checked else '')

    permissions = Permission.objects.all() # 全部Permission
    _permissions = _group.permissions.all() # 用户组里面的Permission

    _all_strs = """"""
    ctypes = ContentType.objects.all().order_by('-app_label')
    for ctype in ctypes:
        import re
        if re.match("^(System|Security|Audit).*", str(ctype.model)):
            continue
        labels = ""
        _lable_arg = [(x.codename, x.name, True) if x in _permissions.filter(content_type=ctype) else
                      (x.codename, x.name, False)
                      for x in permissions.filter(content_type=ctype)]
        for arg in _lable_arg:
            labels += _lable_html(perm_id=arg[0], perm_name=arg[1], checked=arg[2])
        mudule_str = moudle_preform(module_str=ctype.id, module_name=ctype.name.replace('Can ', '能够'), lables=labels)
        _all_strs += mudule_str
    return _all_strs
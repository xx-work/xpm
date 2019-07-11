def test_perm():
    from django.contrib.auth.models import Group, Permission, ContentType

    moudle_preform = lambda module_str, module_name, lables: """<fieldset id="module_{module_str}">
        <legend>{module_name}</legend>{lables}</fieldset>""".format(module_name=module_name, module_str=module_str,
                                                                    lables=lables)
    _lable_html = lambda checked, perm_id, perm_name: """<label class="floating">
            <input type="checkbox" name="role[permissions][]" id="role_permissions_{perm_id}" value="view_changesets" data-shows=".view_changesets_shown" {checked}>
            {perm_name}
            </label>""".format(perm_id=perm_id, perm_name=perm_name, checked='checked="checked"' if checked else '')

    content_types = ContentType.objects.all()
    permitions = Permission.objects.all()

    _group = Group.objects.all()[0]
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
            mudule_str = moudle_preform(module_str=ctype.id, module_name=ctype.name, lables=labels)
            _all_strs += mudule_str
    return _all_strs


if __name__ == '__main__':
    from src import django_setup

    django_setup()
    print(test_perm())
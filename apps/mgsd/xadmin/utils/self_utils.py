from django.utils.safestring import mark_safe


def get_detaild_model(ModelViewAdmin, Model,  objs):
    """
    解决 ManyToManyField 在页面中的显示问题。
    :param ModelViewAdmin: Model的Xadmin类
    :param Model: Model的对象的 ContentType.model_class()
    :param objs: 对象的列表。当前升级版本可以直接传入pks
    :return: 返回渲染后的结果。
    """
    show_detaild = lambda x: """<a data-res-uri="{based_url}{id}/detail/" data-edit-uri="{based_url}{id}/update/" 
            class="details-handler" rel="tooltip" title="{name}"> {name}<i class="fa fa-info-circle"></i> </a>  """.format(
        based_url=ModelViewAdmin.get_model_url(Model, 'changelist'), id=x.id, name=x.name
    )

    links = "<ul><li>" + "</li><li>".join([show_detaild(x) for x in objs]) + "</li></ul>"
    return mark_safe(links)


def get_markd_table_details_show(url, title='预览表格'):
    """
    在 table 中调用 xadmin 的显示;
    :param url:
    :param title:
    :return:
    """
    show_detaild = """<a data-res-uri="{based_url}" data-edit-uri="{based_url2}" class="details-handler" rel="tooltip" title="{name}"> {name} 
    <i class="fa fa-info-circle"></i> </a>  """.format(based_url=url, name=title, based_url2=url.replace('detail', 'update'), )
    return mark_safe(show_detaild)
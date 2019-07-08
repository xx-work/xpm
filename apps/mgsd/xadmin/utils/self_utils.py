
def get_detaild_model(ModelViewAdmin, Model,  objs):

    show_detaild = lambda x: """<a data-res-uri="{based_url}{id}/detail/" data-edit-uri="{based_url}{id}/update/" 
            class="details-handler" rel="tooltip" title="{name}"> {name}<i class="fa fa-info-circle"></i> </a>  """.format(
        based_url=ModelViewAdmin.get_model_url(Model, 'changelist'), id=x.id, name=x.name
    )

    links = "<ul><li>" + "</li><li>".join([show_detaild(x) for x in objs]) + "</li></ul>"
    from django.utils.safestring import mark_safe
    return mark_safe(links)


def get_markd_table_details_show(url, title='预览表格'):

    show_detaild = """<a data-res-uri="{based_url}" class="details-handler" rel="tooltip" title="{name}"> {name} 
    <i class="fa fa-info-circle"></i> </a>  """.format(based_url=url, name=title)
    from django.utils.safestring import mark_safe
    return mark_safe(show_detaild)
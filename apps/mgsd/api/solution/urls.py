from django.conf.urls import url, include

# from .views import urlmap_router
from phaser2.api.hockr.api_views import modify_datafile, add_urlmap, owner_viewer

urlpatterns = [
    ## 默认删除可以调用这个
    # url(r'^patch/', include(urlmap_router.urls)),
    url(r'^modify_patchrule_datafile', modify_datafile),

    ## 默认的增加URLmap的表示
    url(r'^add_urlmap', add_urlmap),
    url(r'^get_owner_viewer', owner_viewer), ## 显示对应的一级视图的列表

]


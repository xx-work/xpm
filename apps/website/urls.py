from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
      url(r'^cso/webmg/', admin.site.urls),
      url(r'^cso/mg/', include("services.urls")),
      url(r'^cso/v1/', include("cso.urls")),
      #url(r'^cso/v1/', include("scan.urls")), ## 管理

  ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
)

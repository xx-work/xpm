from django.conf.urls import url

urlpatterns = [

]


from .api.backer.urls import urlpatterns as backer_up
urlpatterns += backer_up
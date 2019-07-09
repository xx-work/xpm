from django.conf.urls import url

urlpatterns = [

]


from .api.backer.urls import urlpatterns as backer_up
urlpatterns += backer_up


from .api.xobj.views import copfound
urlpatterns += [
    url("^selffdsafdsafdsafdsa", copfound, name="cop_self_found")

]
from django.conf.urls import url

urlpatterns = [

]

from .api.backer.views import backup, recover
urlpatterns += [
    url('backup/1rewq3432frewqrewqfdaf/$', backup, name='backup'),
    url('recover/1rewq3432frewqrewqfdaf/$', recover, name='recover'),
]


from .api.xobj.views import copfound
from .api.chk.views import push2infosec

urlpatterns += [
    url("^selffdsafdsafdsafdsa", copfound, name="cop_self_found"),
    url("^push2infosec", push2infosec, name="push2infosec")
]

from .api.policy.policydetails.views import get_latest_log_policy, get_latest_password_policy
urlpatterns += [
    url("^get_latest_log_policy", get_latest_log_policy, name="get_latest_log_policy"),
    url("^get_latest_password_policy", get_latest_password_policy, name="get_latest_password_policy")
]
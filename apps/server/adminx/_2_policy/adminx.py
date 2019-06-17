import xadmin

from ...models import PolicyBench, PolicyAction, PolicyRule


xadmin.site.register(PolicyBench)
xadmin.site.register(PolicyAction)
xadmin.site.register(PolicyRule)
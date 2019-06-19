import xadmin


from services.models import Community

class CommunityAdmin(object):
    list_display = ("community_name", "group", "responsibility", "date_created")


xadmin.site.register(Community, CommunityAdmin)
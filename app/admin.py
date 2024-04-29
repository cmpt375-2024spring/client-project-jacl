from django.contrib import admin
from app.models import BoardMember, Event, HomePageImage, Statement, JoinUs, MissionVisionStatement, Affiliate, Contact

admin.site.register(Event)
admin.site.register(JoinUs)
admin.site.register(BoardMember)
admin.site.register(HomePageImage)
admin.site.register(MissionVisionStatement)
admin.site.register(Statement)
admin.site.register(Affiliate)
admin.site.register(Contact)

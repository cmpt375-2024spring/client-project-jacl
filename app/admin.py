from django.contrib import admin
from app.models import BoardMember, Event, HomePageImage, MissionVisionStatement


admin.site.register(Event)
admin.site.register(BoardMember)
admin.site.register(HomePageImage)
admin.site.register(MissionVisionStatement)

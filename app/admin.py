from django.contrib import admin
from app.models import BoardMember, Event, HomePageImage, JoinUs


admin.site.register(Event)
admin.site.register(JoinUs)
admin.site.register(BoardMember)
admin.site.register(HomePageImage)

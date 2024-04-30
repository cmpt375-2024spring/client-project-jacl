from django.core.management import call_command
from django.db.models.signals import post_save
import app.models as models


def collect_static(**kwargs):
    print("help")
    call_command('collectstatic', '--noinput')


post_save.connect(collect_static, sender=models.Event, dispatch_uid='post_event_collect_static')
post_save.connect(collect_static, sender=models.Statement, dispatch_uid='post_statement_collect_static')
post_save.connect(collect_static, sender=models.BoardMember, dispatch_uid='post_boardmember_collect_static')
post_save.connect(collect_static, sender=models.HomePageImage, dispatch_uid='post_homepageimage_collect_static')

from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Event(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    banner_image = models.ImageField(upload_to='app/static/user_upload/event_banners/')
    start_date = models.DateField()
    start_time = models.TimeField(null=True, blank=True)
    end_date = models.DateField()
    end_time = models.TimeField(null=True, blank=True)
    location = models.CharField(max_length=255)
    registration_link = models.CharField(max_length=255, null=True, blank=True)
    modified_on = models.DateTimeField(editable=False, auto_now=True)

class HomePageImage(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='app/static/user_upload/homePage')

    def __str__(self):
        return self.title


class BoardMember(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    profile_picture = models.ImageField(upload_to='app/static/user_upload/boardmember/')

    def __str__(self):
        return self.user.get_full_name() if self.user.get_full_name() else self.user.get_username()

    @receiver(post_save, sender=User)  # methods found on https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            BoardMember.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.boardmember.save()


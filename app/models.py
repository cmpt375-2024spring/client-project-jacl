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

    def __str__(self):
        return self.title


class HomePageImage(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='app/static/user_upload/homePage')

    def __str__(self):
        return self.title


class BoardMember(models.Model):
    POSITION_CHOICES = [
        ('1', 'PRESIDENT'),
        ('2', 'TREASURER'),
        ('3', 'SECRETARY'),
        ('4', 'MEMBERSHIP'),
        ('5', 'YOUTH REP'),
        ('6', 'SALT LAKE BUDDHIST TEMPLE LIASON'),
        ('7', 'MATSUMOTO LIASON'),
        ('8', 'PEACH GARDEN LIASON'),
        ('9', 'AT LARGE'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(null=True, default="", blank=True)
    profile_picture = models.ImageField(upload_to='app/static/user_upload/boardmember/', blank=True,
                                        default='app/static/images/logo/JACL_Flower.png')
    position = models.CharField(max_length=1, choices=POSITION_CHOICES, default='1', blank=True)

    def __str__(self):
        return self.user.get_full_name() if self.user.get_full_name() else self.user.get_username()

    # methods found on https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            BoardMember.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.boardmember.save()


class JoinUs(models.Model):
    top_circle = models.TextField()
    mid_circle = models.TextField()
    bottom_circle = models.TextField()

    class Meta:
        verbose_name_plural = 'Join Us'

    def __str__(self):
        return "Join Us Text Field"


class MissionVisionStatement(models.Model):
    mission = models.TextField()
    vision = models.TextField()

    class Meta:
        verbose_name_plural = 'Mission and Vision Statements'

    def __str__(self):
        return "Mission and Vision Statement"


class Statement(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='app/static/user_upload/statement/')
    description = models.TextField()

    def __str__(self):
        return self.title


class Affiliate(models.Model):
    affiliateGroups = [("1", "Japanese Cultural Organizations"),
                       ("2", "Religious Organizations"),
                       ("3", "AANHPI Affiliates"),
                       ("4", "LGBTQIA+ Organizations"),
                       ("5", "Other Affiliates")]

    affiliate_group = models.CharField(max_length=1, choices=affiliateGroups, default='Other Affiliates', blank=True)
    name = models.CharField(max_length=100)
    website = models.CharField(max_length=400)

    def __str__(self):
        return self.name

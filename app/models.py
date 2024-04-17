from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


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
    bio = models.TextField(null = True, default="", blank=True)
    profile_picture = models.ImageField(upload_to='app/static/user_upload/boardmember/', blank=True, default='app/static/images/logo/JACL_Flower.png')
    position = models.CharField(max_length=1, choices=POSITION_CHOICES, default='1', blank=True)

    def __str__(self):
        return self.user.get_full_name() if self.user.get_full_name() else self.user.get_username()

    @receiver(post_save, sender=User)  # methods found on https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            BoardMember.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.boardmember.save()


class JoinUs(models.Model):
    text = models.TextField()

    def __str__(self):
        return "Join Us Text Field"


class MissionVisionStatement(models.Model):
    mission = models.TextField()
    vision = models.TextField()

    def __str__(self):
        return "Mission and Vision Statement"


class Statement(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='app/static/user_upload/statement/')
    description = models.TextField()

    def __str__(self):
        return self.title


class Affiliate(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    website = models.CharField(max_length=400)

    def __str__(self):
        return self.name


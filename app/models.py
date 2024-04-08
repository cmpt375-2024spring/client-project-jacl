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
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(null = True, default = "", blank=True)
    profile_picture = models.ImageField(upload_to='app/static/user_upload/boardmember/', blank = True)
    position = models.CharField(max_length=1, choices=POSITION_CHOICES)
    
    def __str__(self):
        return self.user.get_full_name() if self.user.get_full_name() else self.user.get_username()

    @receiver(post_save, sender=User)  # methods found on https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            BoardMember.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.boardmember.save()

from django.contrib.auth.models import User
from django.db import models


class BoardMember(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    bio = models.TextField()
    image = models.ImageField()

    def __str__(self):
        return self.firstname + " " + self.lastname

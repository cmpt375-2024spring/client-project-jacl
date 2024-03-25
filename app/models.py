from django.db import models
class HomePageImage(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='app/static/user_upload/homePage')

    def __str__(self):
        return self.title




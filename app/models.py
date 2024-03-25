from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    banner_image = models.ImageField(upload_to='app/static/user_uploads/event_banners/')
    start_date = models.DateField()
    start_time = models.TimeField(null=True, blank=True)
    end_date = models.DateField()
    end_time = models.TimeField(null=True, blank=True)
    location = models.CharField(max_length=255)
    registration_link = models.CharField(max_length=255, null=True, blank=True)
    modified_on = models.DateTimeField(editable=False, auto_now=True)

    def __str__(self):
        return self.title
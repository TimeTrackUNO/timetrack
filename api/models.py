from django.db import models
from django.utils import timezone


# Create your models here.
class Movie(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=360)
    year = models.IntegerField(blank=False, null=False)
    rating = models.IntegerField(blank=False, null=False)

    created_date = models.DateTimeField(
        default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()


class TimeTracker(models.Model):
    event_name=models.CharField(max_length=50)
    event_description = models.TextField(max_length=360)
    event_starttime=models.DateTimeField(auto_now_add=True)
    event_endtime=models.DateTimeField(auto_now_add=True)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()


class Events(models.Model):
    eventName= models.CharField(max_length=50)
    eventType=models.CharField(max_length=50)


# Create your models here.

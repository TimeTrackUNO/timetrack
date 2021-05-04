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


class User_Log(models.Model):
    email=models.CharField(max_length=50, null=False)
    name=models.CharField(max_length=100)
    phone=models.IntegerField()
    Date=models.DateTimeField(default=timezone.now)
    Time=models.DateTimeField()

class Date(models.Model):
    Date=models.DateTimeField()
    week=models.IntegerField()
    month=models.IntegerField()

class Time (models.Model):
    hour=models.IntegerField()
    minutes=models.IntegerField()
    seconds=models.IntegerField()

class Tasks(models.Model):
    Task=models.CharField()
    Date=models.DateTimeField()
    hours=models.IntegerField()
    status=models.CharField()


class Events(models.Model):
    eventName= models.CharField(max_length=50)
    eventType=models.CharField(max_length=50)


# Create your models here.

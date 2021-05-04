from rest_framework import serializers
from .models import Movie, TimeTracker, User_Log,Time,Tasks,Date, Events


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('pk', 'name', 'description', 'year', 'rating')


class TimeTrackerSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeTracker
        fields = ('pk', 'event_name', 'event_description')


class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_Log
        fields = ('pk', 'email', 'name')




class timeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Time
        fields = ('hour', 'minutes', 'seconds')

class taskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = ('Task', 'date', 'hours','status')


class dateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Date
        fields = ('date', 'week', 'month')


class eventsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = ('eventName', 'eventType')

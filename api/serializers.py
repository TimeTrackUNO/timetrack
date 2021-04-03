from rest_framework import serializers
from .models import Movie, TimeTracker


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('pk', 'name', 'description', 'year', 'rating')


class TimeTrackerSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeTracker
        fields = ('pk', 'event_name', 'event_description')

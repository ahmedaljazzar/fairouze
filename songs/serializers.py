from rest_framework import serializers

from songs import models


class LyricSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Lyric
        fields = '__all__'


class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Track
        fields = '__all__'


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Person
        fields = '__all__'

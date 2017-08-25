from rest_framework import serializers

from song import models


class LyricSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Lyric
        fields = '__all__'


class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Track
        fields = '__all__'


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Song
        fields = '__all__'


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Artist
        fields = '__all__'


class ComposerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Composer
        fields = '__all__'


class WriterSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Writer
        fields = '__all__'

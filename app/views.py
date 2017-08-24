from rest_framework import viewsets

from app import models, serializers


class LyricViewSet(viewsets.ModelViewSet):
    queryset = models.Lyric.objects.all()
    serializer_class = serializers.LyricSerializer


class TrackViewSet(viewsets.ModelViewSet):
    queryset = models.Track.objects.all()
    serializer_class = serializers.TrackSerializer


class SongViewSet(viewsets.ModelViewSet):
    queryset = models.Song.objects.all()
    serializer_class = serializers.SongSerializer


class ArtistViewSet(viewsets.ModelViewSet):
    queryset = models.Artist.objects.all()
    serializer_class = serializers.ArtistSerializer


class ComposerViewSet(viewsets.ModelViewSet):
    queryset = models.Composer.objects.all()
    serializer_class = serializers.ComposerSerializer


class WriterViewSet(viewsets.ModelViewSet):
    queryset = models.Writer.objects.all()
    serializer_class = serializers.WriterSerializer

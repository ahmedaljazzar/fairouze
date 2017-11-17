from rest_framework import viewsets

from songs import models, serializers


class LyricViewSet(viewsets.ModelViewSet):
    queryset = models.Lyric.objects.all()
    serializer_class = serializers.LyricSerializer


class TrackViewSet(viewsets.ModelViewSet):
    queryset = models.Track.objects.all()
    serializer_class = serializers.TrackSerializer


class PersonViewSet(viewsets.ModelViewSet):
    queryset = models.Person.objects.all()
    serializer_class = serializers.PersonSerializer

from django.conf import settings
from django.contrib.auth.models import User
from django.db import models


class BaseModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Lyric(BaseModel):
    value = models.TextField()
    info = models.TextField(null=True, blank=True)
    creator = models.ForeignKey(User)
    language = models.CharField(
        max_length=2,
        choices=settings.LANGUAGES,
        default=settings.LANGUAGE_CODE,
    )

    def __str__(self):
        return self.value


class Track(BaseModel):
    TYPES = (
        ('s', 'sound'),
        ('v', 'video'),
    )
    url = models.URLField()
    length = models.FloatField()
    info = models.TextField(null=True, blank=True)
    type = models.CharField(max_length=1, choices=TYPES)

    def __str__(self):
        return self.url


class Song(BaseModel):
    name = models.CharField(max_length=100)
    info = models.TextField(null=True, blank=True)
    lyrics = models.OneToOneField(Lyric)
    track = models.OneToOneField(Track)
    language = models.CharField(
        max_length=2,
        choices=settings.LANGUAGES,
        default=settings.LANGUAGE_CODE,
    )

    def __str__(self):
        return self.name


class Artist(BaseModel):
    name = models.CharField(max_length=50)
    info = models.TextField(null=True, blank=True)
    songs = models.ForeignKey(Song, related_name='artist')

    def __str__(self):
        return self.name


class Composer(BaseModel):
    name = models.CharField(max_length=50)
    info = models.TextField(null=True, blank=True)
    songs = models.ForeignKey(Song, related_name='composer')

    def __str__(self):
        return self.name


class Writer(BaseModel):
    name = models.CharField(max_length=50)
    info = models.TextField(null=True, blank=True)
    lyrics = models.ForeignKey(Lyric, related_name='writer')

    def __str__(self):
        return self.name

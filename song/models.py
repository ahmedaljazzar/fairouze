from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

from song.base import BaseModel, Person


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
        ('s', _('sound')),
        ('v', _('video')),
    )
    url = models.URLField()
    length = models.FloatField()
    info = models.TextField(null=True, blank=True)
    type = models.CharField(max_length=1, choices=TYPES)

    def __str__(self):
        return self.url


class Song(BaseModel):
    title = models.CharField(max_length=100)
    info = models.TextField(null=True, blank=True)
    lyrics = models.OneToOneField(Lyric)
    track = models.OneToOneField(Track, null=True)
    language = models.CharField(
        max_length=2,
        choices=settings.LANGUAGES,
        default=settings.LANGUAGE_CODE,
    )

    def __str__(self):
        return self.title


class Artist(Person):
    songs = models.ManyToManyField(
        Song,
        related_name='artists',
        related_query_name='artist',
    )


class Composer(Person):
    songs = models.ManyToManyField(
        Song,
        related_name='composers',
        related_query_name='composer',
    )


class Writer(Person):
    lyrics = models.ManyToManyField(
        Lyric,
        related_name='writers',
        related_query_name='writer',
    )

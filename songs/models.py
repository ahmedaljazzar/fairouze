from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _


class Track(models.Model):
    TYPES = (
        ('s', _('sound')),
        ('v', _('video')),
    )
    url = models.URLField(unique=True)
    length = models.FloatField()
    type = models.CharField(max_length=1, choices=TYPES)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.url


class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    image = models.ImageField(upload_to='people', null=True, blank=True)
    info = models.TextField(null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    @property
    def name(self):
        last_name = self.last_name if self.last_name else ''
        return '{} {}'.format(self.first_name, last_name).strip()

    def __str__(self):
        return self.name

    class Meta:
        unique_together = ('first_name', 'last_name',)


class Lyric(models.Model):
    title = models.CharField(max_length=100)
    value = models.TextField()
    info = models.TextField(null=True, blank=True)
    feature = models.BooleanField(default=False)
    up_votes = models.IntegerField(default=0)
    down_votes = models.IntegerField(default=0)
    track = models.ForeignKey(Track, null=True)
    creator = models.ForeignKey(User)
    artist = models.ForeignKey(Person, null=True, related_name='artist')
    writer = models.ForeignKey(
        Person, blank=True, null=True, related_name='writer')
    composer = models.ForeignKey(
        Person, null=True, blank=True, related_name='composer')

    language = models.CharField(
        max_length=2,
        choices=settings.LANGUAGES,
        default=settings.LANGUAGE_CODE,
    )

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def large_title(self):
        return self.title.split()[0]

    def small_title(self):
        return ' '.join(self.title.split()[1:])

    def __str__(self):
        return self.title

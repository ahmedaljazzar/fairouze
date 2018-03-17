from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models import Q
from django.templatetags.static import static
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
    photo = models.ImageField(upload_to='people', null=True, blank=True)
    cover_photo = models.ImageField(upload_to='people', null=True, blank=True)
    info = models.TextField(null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def photo_url(self):
        if self.photo:
            return self.photo.url

        return static('images/unknown.png')

    def cover_photo_url(self):
        if self.cover_photo:
            return self.cover_photo.url

        return self.photo_url()

    @property
    def name(self):
        last_name = self.last_name if self.last_name else ''
        return '{} {}'.format(self.first_name, last_name).strip()

    def __str__(self):
        return self.name

    class Meta:
        unique_together = ('first_name', 'last_name',)


class Lyric(models.Model):
    title = models.CharField(unique=True, max_length=100)
    value = models.TextField()
    info = models.TextField(null=True, blank=True)
    feature = models.BooleanField(default=False)
    up_votes = models.IntegerField(default=0)
    down_votes = models.IntegerField(default=0)
    track = models.ForeignKey(
        Track, null=True, on_delete=models.CASCADE)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    artist = models.ForeignKey(
        Person,
        null=True,
        related_name='artist',
        on_delete=models.CASCADE)
    writer = models.ForeignKey(
        Person,
        blank=True,
        null=True, related_name='writer',
        on_delete=models.CASCADE)
    composer = models.ForeignKey(
        Person,
        null=True,
        blank=True, related_name='composer',
        on_delete=models.CASCADE)

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

    @classmethod
    def find(cls, query):
        return cls.objects.filter(
            Q(title__icontains=query) |
            Q(value__icontains=query) |
            Q(info__icontains=query) |
            Q(track__url__icontains=query) |
            Q(creator__first_name__icontains=query) |
            Q(creator__last_name__icontains=query) |
            Q(artist__first_name__icontains=query) |
            Q(artist__last_name__icontains=query) |
            Q(artist__info__icontains=query) |
            Q(writer__first_name__icontains=query) |
            Q(writer__last_name__icontains=query) |
            Q(writer__info__icontains=query) |
            Q(composer__first_name__icontains=query) |
            Q(composer__last_name__icontains=query) |
            Q(composer__info__icontains=query)
        ).distinct()

    @classmethod
    def find_by_lyrics(cls, query):
        return cls.objects.filter(
            Q(title__icontains=query) |
            Q(value__icontains=query) |
            Q(info__icontains=query)
        ).distinct()

    @classmethod
    def find_by_track(cls, query):
        return cls.objects.filter(
            track__url__icontains=query
        ).distinct()

    @classmethod
    def find_by_person(cls, query):
        return cls.objects.filter(
            Q(creator__first_name__icontains=query) |
            Q(creator__last_name__icontains=query) |
            Q(artist__first_name__icontains=query) |
            Q(artist__last_name__icontains=query) |
            Q(artist__info__icontains=query) |
            Q(writer__first_name__icontains=query) |
            Q(writer__last_name__icontains=query) |
            Q(writer__info__icontains=query) |
            Q(composer__first_name__icontains=query) |
            Q(composer__last_name__icontains=query) |
            Q(composer__info__icontains=query)
        ).distinct()

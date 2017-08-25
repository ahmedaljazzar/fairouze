from django.contrib.auth.models import User

import factory
from factory.fuzzy import FuzzyFloat

from song import models


class UserFactory(factory.DjangoModelFactory):
    username = factory.Sequence(lambda n: 'user_{}'.format(n))
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')

    class Meta:
        model = User


class LyricFactory(factory.DjangoModelFactory):
    creator = factory.SubFactory(UserFactory)

    class Meta:
        model = models.Lyric


class TrackFactory(factory.DjangoModelFactory):
    length = FuzzyFloat(10)
    url = factory.Faker('url')

    class Meta:
        model = models.Track


class SongFactory(factory.DjangoModelFactory):
    lyrics = factory.SubFactory(LyricFactory)
    track = factory.SubFactory(TrackFactory)
    title = factory.Faker('sentence', nb_words=4)

    class Meta:
        model = models.Song


class ArtistFactory(factory.DjangoModelFactory):
    name = factory.Faker('name')

    class Meta:
        model = models.Artist


class ComposerFactory(factory.DjangoModelFactory):
    name = factory.Faker('name')

    class Meta:
        model = models.Composer


class WriterFactory(factory.DjangoModelFactory):
    name = factory.Faker('name')

    class Meta:
        model = models.Writer

import factory
from factory.fuzzy import FuzzyFloat

from songs import models
from users.factories import UserFactory


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

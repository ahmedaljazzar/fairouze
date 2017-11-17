import factory
from factory.fuzzy import FuzzyFloat

from songs import models
from accounts.factories import UserFactory


class TrackFactory(factory.DjangoModelFactory):
    url = factory.Faker('url')
    length = FuzzyFloat(10)
    type = 's'

    class Meta:
        model = models.Track


class PersonFactory(factory.DjangoModelFactory):
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')

    class Meta:
        model = models.Person


class LyricFactory(factory.DjangoModelFactory):
    value = factory.Faker('sentence', nb_words=120)
    title = factory.Faker('sentence', nb_words=4)
    track = factory.SubFactory(TrackFactory)
    creator = factory.SubFactory(UserFactory)
    artist = factory.SubFactory(PersonFactory)
    composer = factory.SubFactory(PersonFactory)
    writer = factory.SubFactory(PersonFactory)

    class Meta:
        model = models.Lyric

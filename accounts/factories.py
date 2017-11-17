from django.contrib.auth.models import User

import factory

from accounts.models import NewsletterSubscription


class UserFactory(factory.DjangoModelFactory):
    username = factory.Sequence('user_{}'.format)
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')

    class Meta:
        model = User


class SubscriptionFactory(factory.DjangoModelFactory):
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    email = factory.Faker('email')

    class Meta:
        model = NewsletterSubscription

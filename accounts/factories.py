from django.contrib.auth.models import User

import factory


class UserFactory(factory.DjangoModelFactory):
    username = factory.Sequence('user_{}'.format)
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')

    class Meta:
        model = User

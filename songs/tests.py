from django.test import TestCase

from songs.base import Person, BaseModel


class SongBaseTestCase(TestCase):
    def test_base_model(self):
        # Make sure we cannot query it
        with self.assertRaises(AttributeError):
            BaseModel.objects.all()

    def test_person(self):
        # Make sure we cannot query it
        with self.assertRaises(AttributeError):
            Person.objects.all()

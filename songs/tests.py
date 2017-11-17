from django.conf import settings
from django.contrib.auth.models import User
from django.test import TestCase

from songs import factories, models


class SongModelsTestCase(TestCase):
    def test_lyric(self):
        # Ensure everything is normal.
        self.assertEqual(models.Lyric.objects.count(), 0)
        self.assertEqual(User.objects.count(), 0)

        # Lyric factory will create a user object as well.
        factories.LyricFactory.create()
        self.assertEqual(models.Lyric.objects.count(), 1)
        self.assertEqual(User.objects.count(), 1)

        # We only have one value.
        obj = models.Lyric.objects.first()
        self.assertIsNone(obj.info)
        self.assertEqual(obj.language, settings.LANGUAGE_CODE)
        self.assertEqual(str(obj), obj.title)
        self.assertIsInstance(obj.creator, User)

    def test_track(self):
        # Ensure everything is normal.
        self.assertEqual(models.Track.objects.count(), 0)

        # Check tracks types.
        expected_types = (
            ('s', 'sound'),
            ('v', 'video'),
        )
        self.assertEqual(models.Track.TYPES, expected_types)

        # Create a track.
        factories.TrackFactory.create()
        self.assertEqual(models.Track.objects.count(), 1)

        # We only have one value.
        obj = models.Track.objects.first()
        self.assertEqual(str(obj), obj.url)

    def test_person(self):
        # Ensure everything is fine.
        self.assertEqual(models.Person.objects.count(), 0)

        artist = factories.PersonFactory.create()
        self.assertEqual(models.Person.objects.count(), 1)

        # No songs assigned to any artist.
        songs = models.Lyric.objects.all()
        self.assertFalse(songs.exists())

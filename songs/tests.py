from django.conf import settings
from django.contrib.auth.models import User
from django.db import IntegrityError, transaction
from django.test import TestCase

from songs import factories, models
from songs.base import Person, BaseModel


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
        self.assertEqual(str(obj), obj.value)
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
        self.assertIsNone(obj.info)
        self.assertEqual(str(obj), obj.url)

    def test_song(self):
        # Ensure everything is normal.
        self.assertEqual(models.Song.objects.count(), 0)
        self.assertEqual(models.Lyric.objects.count(), 0)

        # Lyric factory will create a user object as well.
        obj = factories.SongFactory.create()
        self.assertEqual(models.Song.objects.count(), 1)
        self.assertEqual(models.Lyric.objects.count(), 1)

        # We didn't create info.
        self.assertIsNone(obj.info)
        self.assertEqual(str(obj), obj.title)
        self.assertIsInstance(obj.title, str)

        # A song can only has one lyrics object, and a lyrics object
        # can only be assigned to one Song.
        with self.assertRaises(IntegrityError), transaction.atomic():
            factories.SongFactory.create(lyrics=obj.lyrics)

        # A song can only has one track, and a track can only
        # be assigned to one Song.
        with self.assertRaises(IntegrityError), transaction.atomic():
            factories.SongFactory.create(track=obj.track)

        # Make sure every thing still as it was after the failed
        # creations.
        self.assertEqual(models.Song.objects.count(), 1)
        self.assertEqual(models.Lyric.objects.count(), 1)

    def test_artist(self):
        # Ensure everything is fine.
        self.assertEqual(models.Artist.objects.count(), 0)

        artist = factories.ArtistFactory.create()
        self.assertEqual(models.Artist.objects.count(), 1)

        # No songs assigned to this artist.
        self.assertFalse(artist.songs.exists())

        song1 = factories.SongFactory.create()
        song2 = factories.SongFactory.create()
        self.assertEqual(models.Song.objects.count(), 2)

        # Assign some songs to the artist.
        artist.songs.add(song1)
        self.assertEqual(artist.songs.count(), 1)
        self.assertEqual(song1.artists.all()[0], artist)

        artist.songs.add(song2)
        self.assertEqual(artist.songs.count(), 2)
        self.assertEqual(song1.artists.all()[0], artist)

        # Ensure we can filter songs assigned to artists.
        self.assertTrue(models.Song.objects.filter(artist=artist))
        self.assertEqual(
            models.Song.objects.filter(artist=artist).count(), 2)

    def test_composer(self):
        # Ensure everything is fine
        self.assertEqual(models.Composer.objects.count(), 0)

        composer = factories.ComposerFactory.create()
        self.assertEqual(models.Composer.objects.count(), 1)

        # No songs assigned to this composer
        self.assertFalse(composer.songs.exists())

        song1 = factories.SongFactory.create()
        song2 = factories.SongFactory.create()
        self.assertEqual(models.Song.objects.count(), 2)

        # Assign some songs to the composer
        composer.songs.add(song1)
        self.assertEqual(composer.songs.count(), 1)
        self.assertEqual(song1.composers.all()[0], composer)

        composer.songs.add(song2)
        self.assertEqual(composer.songs.count(), 2)
        self.assertEqual(song1.composers.all()[0], composer)

        # Ensure we can filter songs assigned to composers
        self.assertTrue(models.Song.objects.filter(composer=composer))
        self.assertEqual(
            models.Song.objects.filter(composer=composer).count(), 2)

    def test_writer(self):
        # Ensure everything is fine.
        self.assertEqual(models.Writer.objects.count(), 0)

        writer = factories.WriterFactory.create()
        self.assertEqual(models.Writer.objects.count(), 1)

        # No lyrics assigned to the writer yet.
        self.assertFalse(writer.lyrics.exists())

        # No songs assigned to this artist.
        lyric1 = factories.LyricFactory.create()
        lyric2 = factories.LyricFactory.create()
        self.assertEqual(models.Lyric.objects.count(), 2)

        # Assign some lyrics to the writer.
        writer.lyrics.add(lyric1)
        self.assertEqual(writer.lyrics.count(), 1)
        self.assertEqual(lyric1.writers.all()[0], writer)

        writer.lyrics.add(lyric2)
        self.assertEqual(writer.lyrics.count(), 2)
        self.assertEqual(lyric1.writers.all()[0], writer)

        # Ensure we can filter lyrics assigned to writers.
        self.assertTrue(models.Lyric.objects.filter(writer=writer))
        self.assertEqual(
            models.Lyric.objects.filter(writer=writer).count(), 2)


class SongBaseTestCase(TestCase):
    def test_base_model(self):
        # Make sure we cannot query it
        with self.assertRaises(AttributeError):
            BaseModel.objects.all()

    def test_person(self):
        # Make sure we cannot query it
        with self.assertRaises(AttributeError):
            Person.objects.all()

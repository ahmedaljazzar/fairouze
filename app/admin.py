from django.contrib import admin

from app.models import (
    Lyric,
    Track,
    Song,
    Artist,
    Composer,
    Writer,
)


class LyricAdmin(admin.ModelAdmin):
    pass


class TrackAdmin(admin.ModelAdmin):
    pass


class SongAdmin(admin.ModelAdmin):
    pass


class ArtistAdmin(admin.ModelAdmin):
    pass


class ComposerAdmin(admin.ModelAdmin):
    pass


class WriterAdmin(admin.ModelAdmin):
    pass

admin.site.register(Lyric, LyricAdmin)
admin.site.register(Track, TrackAdmin)
admin.site.register(Song, SongAdmin)
admin.site.register(Artist, ArtistAdmin)
admin.site.register(Composer, ComposerAdmin)
admin.site.register(Writer, WriterAdmin)

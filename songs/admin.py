from django.contrib import admin

from songs import models


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


admin.site.register(models.Lyric, LyricAdmin)
admin.site.register(models.Track, TrackAdmin)
admin.site.register(models.Song, SongAdmin)
admin.site.register(models.Artist, ArtistAdmin)
admin.site.register(models.Composer, ComposerAdmin)
admin.site.register(models.Writer, WriterAdmin)

from django.contrib import admin

from songs import models


class LyricAdmin(admin.ModelAdmin):
    pass


class TrackAdmin(admin.ModelAdmin):
    pass


class PersonAdmin(admin.ModelAdmin):
    pass


admin.site.register(models.Lyric, LyricAdmin)
admin.site.register(models.Track, TrackAdmin)
admin.site.register(models.Person, PersonAdmin)

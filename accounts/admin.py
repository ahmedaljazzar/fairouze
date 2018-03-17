from django.contrib import admin

from accounts import models


def resolve(modelAdmin, request, queryset):
    queryset.update(resolved=True)


class LettersAdmin(admin.ModelAdmin):
    list_display = ['email', 'user', ]


class ContactRequestAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'resolved', ]
    actions = [resolve]

    def has_add_permission(self, request):
        return False


admin.site.register(models.NewsletterSubscription, LettersAdmin)
admin.site.register(models.ContactRequest, ContactRequestAdmin)

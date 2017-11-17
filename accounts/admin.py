from django.contrib import admin

from accounts import models


class SubscriptionAdmin(admin.ModelAdmin):
    pass


admin.site.register(models.NewsletterSubscription, SubscriptionAdmin)

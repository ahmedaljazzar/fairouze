from django.contrib.auth.models import User
from django.db import models


class NewsletterSubscription(models.Model):
    user = models.ForeignKey(User, null=True, editable=False)
    email = models.EmailField(unique=True)

    def save(self, **kwargs):
        try:
            self.user = User.objects.get(email=self.email)
        except User.DoesNotExist:
            pass

        return super(NewsletterSubscription, self).save(**kwargs)


class ContactRequest(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    telephone = models.CharField(max_length=75, null=True, blank=True)
    message = models.TextField()
    resolved = models.BooleanField(default=False)

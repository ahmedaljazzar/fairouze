from django.contrib.auth.models import User
from django.db import models


class NewsletterSubscription(models.Model):
    user = models.ForeignKey(
        User, null=True, editable=False, on_delete=models.CASCADE)
    email = models.EmailField(unique=True)

    # NOQA pylint: disable=arguments-differ
    def save(self, **kwargs):
        """
        - This is to inject the user object if the email has been
          recognised, passing to None User if not.

        - I disabled the arguments-differ as all arguments are kwargs
        """
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

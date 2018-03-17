from django import forms
from django.utils.translation import ugettext_lazy as _

from accounts import models


class ContactRequestForm(forms.ModelForm):
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': _('Name')}))
    email = forms.EmailField(
        widget=forms.TextInput(attrs={'placeholder': _('Email')}))
    telephone = forms.RegexField(
        regex=r'^\+?1?\d{9,15}$',
        max_length=75, required=False,
        widget=forms.TextInput(attrs={'placeholder': _('Telephone')}),
        error_messages={
            'invalid': _('Must be entered in the format: +999999999. '
                         'Up to 15 digits.')})
    message = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': _('Message')}))

    class Meta:
        model = models.ContactRequest
        exclude = ('resolved', )

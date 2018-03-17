"""
These are temporary views that must be removed once the UI server is
done.
"""
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView

from accounts import forms
from songs.models import Lyric


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)

        context['latest'] = Lyric.objects.order_by('-created')[:4]
        context['featured'] = Lyric.objects\
            .filter(feature=True)\
            .order_by('-created')

        top_songs = Lyric.objects.order_by('-up_votes')[:10]
        context['top'] = top_songs
        context['top_song'] = top_songs.first()

        return context


class ContactsView(FormView):
    form_class = forms.ContactRequestForm
    template_name = 'contacts.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.save(commit=True)
        return super(ContactsView, self).form_valid(form)


def djs_and_shows_view(request):
    return render(request, 'index-1.html', {})


def events_view(request):
    return render(request, 'index-2.html', {})


def news_view(request):
    return render(request, 'index-3.html', {})


def schedule_view(request):
    return render(request, 'index-4.html', {})


def policy_view(request):
    return render(request, 'index-6.html', {})

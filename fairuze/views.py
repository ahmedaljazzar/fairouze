"""
These are temporary views that must be removed once the UI server is
done.
"""
from django.shortcuts import render
from django.views.generic import TemplateView

from songs.models import Lyric


class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)

        context['latest'] = Lyric.objects.order_by('-created')[:5]
        context['featured'] = Lyric.objects\
            .filter(feature=True)\
            .order_by('-created')


        return context


def djs_and_shows_view(request):
    return render(request, 'index-1.html', {})


def events_view(request):
    return render(request, 'index-2.html', {})


def news_view(request):
    return render(request, 'index-3.html', {})


def schedule_view(request):
    return render(request, 'index-4.html', {})


def contacts_view(request):
    return render(request, 'index-5.html', {})


def policy_view(request):
    return render(request, 'index-6.html', {})

"""
These are temporary views that must be removed once the UI server is
done.
"""
from django.shortcuts import render


def home_view(request):
    return render(request, 'index.html', {})


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

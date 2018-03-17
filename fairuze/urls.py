"""fairuze URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from rest_framework import routers
from rest_framework.documentation import include_docs_urls

from fairuze import views
from songs import views as songs_views
from accounts import views as accounts_views


# API Routers
router = routers.DefaultRouter()
router.register(r'lyrics', songs_views.LyricViewSet)
router.register(r'tracks', songs_views.TrackViewSet)
router.register(r'persons', songs_views.PersonViewSet)
router.register(r'accounts', accounts_views.AccountsViewSet,
                base_name='accounts')
router.register(r'newsletters', accounts_views.SubscriptionViewSet,
                base_name='newsletters')


# URL Patterns
urlpatterns = [

    # This view should be removed.
    path('', views.HomeView.as_view(), name='home'),
    path('djs/', views.djs_and_shows_view, name='djs'),
    path('events/', views.events_view, name='events'),
    path('news/', views.news_view, name='news'),
    path('schedule/', views.schedule_view, name='schedule'),
    path('contacts/', views.ContactsView.as_view(), name='contacts'),
    path('policy/', views.policy_view, name='policy'),
    path('search/', views.SearchView.as_view(), name='search'),

    path('admin/', admin.site.urls),

    # API URLs
    path('api/', include('rest_framework.urls')),
    path('api/', include(router.urls)),

    # Documentations URLs
    path('docs/api/', include_docs_urls(title='Fairuze API Guide')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

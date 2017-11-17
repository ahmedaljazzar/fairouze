"""fairuze URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.conf.urls import url, include

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


# URL Patterns
urlpatterns = [

    # This view should be removed.
    url(r'^$', views.HomeView.as_view(), name='home'),
    url(r'^djs/$', views.djs_and_shows_view, name='djs'),
    url(r'^events/$', views.events_view, name='events'),
    url(r'^news/$', views.news_view, name='news'),
    url(r'^schedule/$', views.schedule_view, name='schedule'),
    url(r'^contacts/$', views.contacts_view, name='contacts'),
    url(r'^policy/$', views.policy_view, name='policy'),

    url(r'^admin/', admin.site.urls),

    # API URLs
    url(r'^api/', include('rest_framework.urls')),
    url(r'^api/', include(router.urls)),

    # Documentations URLs
    url(r'^docs/api/', include_docs_urls(title='Fairuze API Guide')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

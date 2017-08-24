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
from django.contrib import admin
from django.conf.urls import url, include

from rest_framework import routers

from app import views


# API Routers
router = routers.DefaultRouter()
router.register(r'lyrics', views.LyricViewSet)
router.register(r'tracks', views.TrackViewSet)
router.register(r'songs', views.SongViewSet)
router.register(r'artists', views.ArtistViewSet)
router.register(r'composers', views.ComposerViewSet)
router.register(r'writers', views.WriterViewSet)


# URL Patterns
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/',
        include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/', include(router.urls, namespace='api')),
]

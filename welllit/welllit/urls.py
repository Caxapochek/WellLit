"""welllit URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from django.views.generic.base import RedirectView

from . import settings
from ceiling.views import *

from ceiling.sitemaps import StaticViewSitemap, PortfolioSitemap

sitemaps = {
    'static': StaticViewSitemap,
    'portfolio': PortfolioSitemap,
}

favicon_view = RedirectView.as_view(url='/static/ceiling/favicon/favicon.ico', permanent=True)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}),
    re_path(r'^favicon\.ico$', favicon_view),
    path('', include('ceiling.urls')),
    path('captcha/', include('captcha.urls'))
]

handler404 = pageNotFound

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
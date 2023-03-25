from django.urls import path
from django.views.generic.base import TemplateView

from .views import *

urlpatterns = [
    path('', MainPage.as_view(), name='main'),
    path('info/installation-procedure/', InstallationPage.as_view(), name='installation-procedure'),
    path('info/colors-and-textures/', ColorsAndTexturesPage.as_view(), name='colors-and-textures'),
    path('contactus/', ContactUsPage.as_view(), name='contactus'),
    path('price-list/', PriceListPage.as_view(), name='price-list'),
    path('calculator/', СalculatorPage.as_view(), name='calculator'),
    path('portfolio/', PortfolioPage.as_view(), name='portfolio'),
    path('portfolio/<slug:portfolioitem_slug>/', PortfolioItemPage.as_view(), name='portfolio-item'),
    path(
        'robots.txt/',
        TemplateView.as_view(template_name="ceiling/robots.txt", content_type="text/plain"),
    ),
]
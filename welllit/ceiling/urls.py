from django.urls import path

from .views import *

urlpatterns = [
    path('', MainPage.as_view(), name='main'),
    path('info/installation-procedure/', InstallationPage.as_view(), name='installation-procedure'),
    path('info/colors-and-textures/', ColorsAndTexturesPage.as_view(), name='colors-and-textures'),
    path('contactus/', ContactUsPage.as_view(), name='contactus'),
    path('price-list/', PriceListPage.as_view(), name='price-list'),
    path('calculator/', СalculatorPage.as_view(), name='calculator'),
    path('portfolio/', PortfolioPage.as_view(), name='portfolio')
]
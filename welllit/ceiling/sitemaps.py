from django.contrib.sitemaps import Sitemap 
from django.urls import reverse
from ceiling.models import Portfolio

class PortfolioSitemap(Sitemap):
    changefreq = 'monthly'
    priority = 0.5

    def items(self):
        return Portfolio.objects.all()

class StaticViewSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return [
            'main',
            'installation-procedure', 
            'colors-and-textures',
            'contactus',
            'price-list',
            'calculator',
            'portfolio']

    def location(self, item):
        return reverse(item)


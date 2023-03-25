from django.contrib import admin
from django.utils.safestring import mark_safe

# Register your models here.

from .models import *

class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('name','phone','email','date')
    list_display_links = ('name',)
    search_fields = ('name',)
    list_filter = ('date',)


class CeilingsAdmin(admin.ModelAdmin):
    list_display = ('model','color','price','availability')
    list_display_links = ('model',)
    search_fields = ('model',)
    list_filter = ('model',)


class ServicesAdmin(admin.ModelAdmin):
    list_display = ('name','measurement','price')
    list_display_links = ('name',)
    search_fields = ('name',)


class portfolioAdmin(admin.ModelAdmin):
    list_display = ('id','title','square','room', 'material','price')
    list_display_links = ('title',)
    search_fields = ('room','material', 'invoice', 'color', 'section')
    list_filter = ('room','material', 'invoice', 'color', 'section')
    prepopulated_fields = {'slug': ('title','price')}


class portfoliofotoAdmin(admin.ModelAdmin):
    list_display = ('id','portfolioID','img','main')
    list_display_links = ('portfolioID','img')
    search_fields = ('portfolioID',)
    list_filter = ('portfolioID',)
    
    def get_html_photo(self, object):
        if object.photo:
            return mark_safe(f"<img src='{object.photo.url}' width=50>")
    get_html_photo.short_description = "Миниатюра"


admin.site.register(Application, ApplicationAdmin)
admin.site.register(Celings, CeilingsAdmin)
admin.site.register(Services, ServicesAdmin)
admin.site.register(Portfolio, portfolioAdmin)
admin.site.register(PortfolioPhoto, portfoliofotoAdmin)
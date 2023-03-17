from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView
from django.urls import reverse_lazy

from .models import Application
from .utils import DataMixin
from .forms import *

# Create your views here.

class MainPage(DataMixin, CreateView):
    form_class = ApplicationForm
    template_name = 'ceiling/main.html'
    success_url = reverse_lazy('main')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        mixin_context = self.get_user_context(title = 'Главная страница')
        context = dict(list(context.items()) + list(mixin_context.items()))
        return context


class InstallationPage(DataMixin, TemplateView):
    template_name = 'ceiling/installation-procedure.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        mixin_context = self.get_user_context(title = 'Процедура установки')
        context = dict(list(context.items()) + list(mixin_context.items()))
        return context


class ColorsAndTexturesPage(DataMixin, TemplateView):
    template_name = 'ceiling/colors-and-textures.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        mixin_context = self.get_user_context(title = 'Цвета и фактуры')
        context = dict(list(context.items()) + list(mixin_context.items()))
        return context


class ContactUsPage(DataMixin, CreateView):
    form_class = ApplicationForm
    template_name = 'ceiling/contactus.html'
    success_url = reverse_lazy('main')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        mixin_context = self.get_user_context(title = 'Контакты')
        context = dict(list(context.items()) + list(mixin_context.items()))
        return context


class PriceListPage(DataMixin, ListView):
    template_name = 'ceiling/price-list.html'
    model = Celings
    context_object_name = 'celings'
    ceilings = Celings.objects.all()
    models = Celings.objects.values_list('model', flat=True).distinct()
    colors = dict.fromkeys(Celings.objects.values_list('color', flat=True).distinct())
    for k, v in colors.items():
        colors[k] = {} | dict.fromkeys(models, '-').copy()
    for ceiling in ceilings: 
        c1 = colors[ceiling.color][ceiling.model] = str(ceiling.price)

    extra_context = {'ceilings_pivot': colors,
                     'models': models,
                     'services': Services.objects.all()}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        mixin_context = self.get_user_context(title = 'Прайс-лист')
        context = dict(list(context.items()) + list(mixin_context.items()))
        return context


class СalculatorPage(DataMixin, TemplateView):
    template_name = 'ceiling/calculator.html'
    extra_context = {'ceilings': Celings.objects.all()}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        mixin_context = self.get_user_context(title = 'Калькулятор')
        context = dict(list(context.items()) + list(mixin_context.items()))
        return context


class PortfolioPage(DataMixin, ListView):
    template_name = 'ceiling/portfolio.html'
    model = Portfolio
    context_object_name = 'portfolio'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        mixin_context = self.get_user_context(title = 'Наши работы')
        context = dict(list(context.items()) + list(mixin_context.items()))
        return context
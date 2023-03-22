from django.http import HttpResponseNotFound
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
        mixin_context = self.get_user_context(title = 'Главная страница',
                                              description = 'Сайт компания Welllit. Монтаж натяжных потолков под ключ в Ярославле.',
                                              keywords = 'welllit, велит, натяжной, потолок, ярославль, монтаж')
        context = dict(list(context.items()) + list(mixin_context.items()))
        return context


class InstallationPage(DataMixin, TemplateView):
    template_name = 'ceiling/installation-procedure.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        mixin_context = self.get_user_context(title = 'Процесс монтажа',
                                              description = 'Описание процесса монтажа натяжных потолков. Инструменты, шаги, материалы.',
                                              keywords = 'welllit, велит, натяжной, потолок, процесс, монтаж, шаги')
        context = dict(list(context.items()) + list(mixin_context.items()))
        return context


class ColorsAndTexturesPage(DataMixin, TemplateView):
    template_name = 'ceiling/colors-and-textures.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        mixin_context = self.get_user_context(title = 'Цвета и фактуры',
                                              description = 'Какие бывают натяжные потолки? Формы, материалы, фактуры, цвета.',
                                              keywords = 'welllit, велит, натяжной, потолок, формы, материалы, фактуры, цвета, пвх, тканевая, матовый, глянцевый, сатиновый')
        context = dict(list(context.items()) + list(mixin_context.items()))
        return context


class ContactUsPage(DataMixin, CreateView):
    form_class = ApplicationForm
    template_name = 'ceiling/contactus.html'
    success_url = reverse_lazy('main')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        mixin_context = self.get_user_context(title = 'Контакты',
                                              description = 'Оставьте заявку на сайте или свяжитесь с нами любым, удобным для вас, способом. ',
                                              keywords = 'welllit, велит, натяжной, потолок, контакты, купитьб заказать')
        context = dict(list(context.items()) + list(mixin_context.items()))
        return context


class PriceListPage(DataMixin, ListView):
    template_name = 'ceiling/price-list.html'
    model = Celings
    context_object_name = 'celings'
    ceilings = Celings.objects.all()
    models = Celings.objects.values_list('model', flat=True).distinct().order_by('model')
    colors = dict.fromkeys(Celings.objects.values_list('color', flat=True).distinct().order_by('color'))
    for k, v in colors.items():
        colors[k] = {} | dict.fromkeys(models, '-').copy()
    for ceiling in ceilings: 
        c1 = colors[ceiling.color][ceiling.model] = str(ceiling.price)

    extra_context = {'ceilings_pivot': colors,
                     'models': models,
                     'services': Services.objects.all()}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        mixin_context = self.get_user_context(title = 'Прайс-лист',
                                              description = 'Актуальные цены на материалы, работы и услуги, которые мы предлагаем.',
                                              keywords = 'welllit, велит, натяжной, потолок, полотно,  цены, прайс-лист, ярославль')
        context = dict(list(context.items()) + list(mixin_context.items()))
        return context


class СalculatorPage(DataMixin, TemplateView):
    template_name = 'ceiling/calculator.html'
    extra_context = {'ceilings': Celings.objects.all()}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        mixin_context = self.get_user_context(title = 'Калькулятор',
                                              description = 'Калькулятор расчета стоимости натяжного потолка. Посчитайте сколько будет стоить установка по вашим замерам.',
                                              keywords = 'welllit, велит, натяжной, потолок, калькулятор, цена, посчитать')
        context = dict(list(context.items()) + list(mixin_context.items()))
        return context


class PortfolioPage(DataMixin, ListView):
    template_name = 'ceiling/portfolio.html'
    model = Portfolio
    context_object_name = 'portfolio'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        mixin_context = self.get_user_context(title = 'Наши работы',
                                              description = 'Наше портфолио. Здесь можно ознакомиться с работами, которые мы производили.',
                                              keywords = 'welllit, велит, натяжной, потолок, портфолио, работа, галерея, пример')
        context = dict(list(context.items()) + list(mixin_context.items()))
        return context

def pageNotFound(request, exception):
    main_url = reverse_lazy('main')
    return HttpResponseNotFound(f'<h1>Страница не найдена</h1><a href="{main_url}">На главную</a>')
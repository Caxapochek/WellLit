from django.db import models
from django.urls import reverse

# Create your models here.

class Application(models.Model):
    name = models.CharField(max_length=255, null=False, verbose_name='Имя')
    phone = models.CharField(max_length=16, null=False, verbose_name='Телефон')
    email = models.EmailField(max_length=255, null=True, blank=True, verbose_name='Почта')
    date = models.DateTimeField(auto_now=True, null=False, verbose_name='Дата')
    comment = models.TextField(max_length=2000, null=True, blank=True, verbose_name='Комментарий')


    def __str__(self):
        return f"{self.name}:\n \
        Телефон: {self.phone}\n \
        Почта: {self.email}\n \
        Дата: {self.date}\n \
        Комментарий: {self.comment}"
    

    # def get_absolute_url(self):
    #     return reverse('application', kwargs={'applicationid':self.id})


    class Meta:
        verbose_name = 'Заявки'
        verbose_name_plural = 'Заявки'
        ordering = ['date', 'name']


class Celings(models.Model):
    model = models.CharField(max_length=255, null=False, verbose_name='Модель')
    color = models.CharField(max_length=255, null=True, verbose_name='Цвет')
    price = models.IntegerField(null=False, verbose_name='Цена')
    availability = models.BooleanField(verbose_name='Наличие')
    

    def __str__(self):
        return f"{self.model}:\n \
        Цвет: {self.color}\n \
        Цена: {self.price}\n \
        Наличие: {'да' if self.availability else 'нет'}"
    

    class Meta:
        verbose_name = 'Полотна'
        verbose_name_plural = 'Полотна'


class Services(models.Model):
    name = models.CharField(max_length=255, null=False, verbose_name='Наименование')
    measurement = models.CharField(max_length=255, null=False, verbose_name='Еденицы измерения')
    price = models.IntegerField(null=False, verbose_name='Цена')
    

    def __str__(self):
        return f"{self.name}:\n \
        Ед. изм.: {self.measurement}\n \
        Цена: {self.price}"
    

    class Meta:
        verbose_name = 'Услуги'
        verbose_name_plural = 'Услуги'


class Portfolio(models.Model):
    title = models.CharField(max_length=255, null=False, verbose_name='Загаловок', default='')
    square = models.FloatField(null=False, verbose_name='Площадь', default=0)
    room = models.CharField(max_length=255, null=False, verbose_name='Помещение', default='')
    material = models.CharField(max_length=255, null=False, verbose_name='Материял', default='')
    invoice = models.CharField(max_length=255, null=False, verbose_name='Фактура', default='')
    color = models.CharField(max_length=255, null=False, verbose_name='Цвет', default='')
    corners = models.IntegerField(null=False, verbose_name='Углы', default=0)
    section = models.CharField(max_length=255, null=False, verbose_name='Профиль', default='')
    light = models.IntegerField(null=False, verbose_name='Точек света', default=0)
    pipe = models.IntegerField(null=False, verbose_name='Обходов труб', default=0)
    price = models.IntegerField(null=False, verbose_name='Цена', default=0)
    description = models.CharField(max_length=255, null=False, verbose_name='Описание', default='')
    slug = models.SlugField(max_length=255, unique=True, null=False, db_index=True, verbose_name='URL')
    
    def get_absolute_url(self):
        return reverse('portfolio-item', kwargs={'portfolioitem_slug': f'{self.slug}'})

    class Meta:
        verbose_name = 'Карточка портфолио'
        verbose_name_plural = 'Карточки портфолио'


class PortfolioPhoto(models.Model):
    portfolioID = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='photos/',null=False, verbose_name='Фото')
    main = models.BooleanField(verbose_name='Первое фото')
    

    class Meta:
        verbose_name = 'Фотография к портфолио'
        verbose_name_plural = 'Фотографии к портфолио'
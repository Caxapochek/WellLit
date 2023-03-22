# Generated by Django 4.1.7 on 2023-03-22 06:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Имя')),
                ('phone', models.CharField(max_length=16, verbose_name='Телефон')),
                ('email', models.EmailField(blank=True, max_length=255, null=True, verbose_name='Почта')),
                ('date', models.DateTimeField(auto_now=True, verbose_name='Дата')),
                ('comment', models.TextField(blank=True, max_length=2000, null=True, verbose_name='Комментарий')),
            ],
            options={
                'verbose_name': 'Заявки',
                'verbose_name_plural': 'Заявки',
                'ordering': ['date', 'name'],
            },
        ),
        migrations.CreateModel(
            name='Celings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=255, verbose_name='Модель')),
                ('color', models.CharField(max_length=255, null=True, verbose_name='Цвет')),
                ('price', models.IntegerField(verbose_name='Цена')),
                ('availability', models.BooleanField(verbose_name='Наличие')),
            ],
            options={
                'verbose_name': 'Полотна',
                'verbose_name_plural': 'Полотна',
            },
        ),
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Описание')),
                ('square', models.FloatField(verbose_name='Площадь')),
                ('room', models.CharField(max_length=255, verbose_name='Помещение')),
                ('material', models.CharField(max_length=255, verbose_name='Материял')),
                ('invoice', models.CharField(max_length=255, verbose_name='Фактура')),
                ('color', models.CharField(max_length=255, verbose_name='Цвет')),
                ('corners', models.IntegerField(verbose_name='Углы')),
                ('section', models.CharField(max_length=255, verbose_name='Профиль')),
                ('light', models.IntegerField(verbose_name='Точек света')),
                ('pipe', models.IntegerField(verbose_name='Обходов труб')),
                ('price', models.IntegerField(verbose_name='Цена')),
            ],
            options={
                'verbose_name': 'Карточка портфолио',
                'verbose_name_plural': 'Карточки портфолио',
            },
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Наименование')),
                ('measurement', models.CharField(max_length=255, verbose_name='Еденицы измерения')),
                ('price', models.IntegerField(verbose_name='Цена')),
            ],
            options={
                'verbose_name': 'Услуги',
                'verbose_name_plural': 'Услуги',
            },
        ),
        migrations.CreateModel(
            name='PortfolioPhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='photos/', verbose_name='Фото')),
                ('main', models.BooleanField(verbose_name='Первое фото')),
                ('portfolioID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ceiling.portfolio')),
            ],
            options={
                'verbose_name': 'Фотография к портфолио',
                'verbose_name_plural': 'Фотографии к портфолио',
            },
        ),
    ]

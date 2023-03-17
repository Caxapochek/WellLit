# Generated by Django 4.1.7 on 2023-03-10 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ceiling', '0002_celings'),
    ]

    operations = [
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
    ]
# Generated by Django 4.1.7 on 2023-03-16 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ceiling', '0009_alter_portfoliophoto_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfoliophoto',
            name='main',
            field=models.BooleanField(default=False, verbose_name='Первое фото'),
            preserve_default=False,
        ),
    ]
# Generated by Django 4.1.7 on 2023-03-30 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ceiling', '0005_alter_portfolio_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='description',
            field=models.CharField(blank=True, default='', max_length=255, null=True, verbose_name='Описание'),
        ),
    ]

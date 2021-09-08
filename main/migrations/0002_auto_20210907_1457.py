# Generated by Django 3.2.6 on 2021-09-07 12:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asset',
            name='asset_endDate',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 7, 14, 57, 58, 620474), verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='asset',
            name='asset_startDate',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 7, 14, 57, 58, 620474), verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='asset',
            name='asset_value',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='owner',
            name='owner_revenue',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='tenant',
            name='tenant_revenue',
            field=models.IntegerField(),
        ),
    ]
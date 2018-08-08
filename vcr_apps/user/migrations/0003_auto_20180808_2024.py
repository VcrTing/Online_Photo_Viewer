# Generated by Django 2.0.5 on 2018-08-08 12:24

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20180808_1713'),
    ]

    operations = [
        migrations.AddField(
            model_name='kouzactrl',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 8, 8, 12, 24, 37, 165555, tzinfo=utc), verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='kouza',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 8, 8, 12, 24, 37, 166552, tzinfo=utc), verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='kouzactrl',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 8, 8, 12, 24, 37, 165555, tzinfo=utc), verbose_name='最近更新时间'),
        ),
    ]

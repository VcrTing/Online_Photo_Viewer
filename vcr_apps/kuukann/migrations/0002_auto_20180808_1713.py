# Generated by Django 2.0.5 on 2018-08-08 09:13

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('kuukann', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='img',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 8, 8, 9, 13, 18, 986371, tzinfo=utc), verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='kuukann',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 8, 8, 9, 13, 18, 983380, tzinfo=utc), verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='pic',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 8, 8, 9, 13, 18, 985377, tzinfo=utc), verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='pic',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 8, 8, 9, 13, 18, 985377, tzinfo=utc), verbose_name='最近更新时间'),
        ),
        migrations.AlterField(
            model_name='picmsg',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 8, 8, 9, 13, 18, 985377, tzinfo=utc), verbose_name='创建时间'),
        ),
    ]

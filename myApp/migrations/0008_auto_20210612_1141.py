# Generated by Django 3.1.1 on 2021-06-12 06:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0007_auto_20210612_1125'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 6, 12, 11, 41, 9, 310461)),
        ),
    ]

# Generated by Django 3.1.1 on 2021-05-27 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='Uploads/Products/'),
        ),
    ]
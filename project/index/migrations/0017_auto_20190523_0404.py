# Generated by Django 2.0 on 2019-05-23 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0016_auto_20190523_0402'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poster',
            name='Price',
            field=models.PositiveIntegerField(),
        ),
    ]
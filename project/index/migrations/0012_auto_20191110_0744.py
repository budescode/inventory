# Generated by Django 2.0 on 2019-11-10 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0011_auto_20191110_0355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='index',
            name='name',
            field=models.CharField(blank=True, max_length=90, null=True),
        ),
    ]

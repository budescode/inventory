# Generated by Django 2.0 on 2019-11-10 02:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0010_auto_20191109_0559'),
    ]

    operations = [
        migrations.AlterField(
            model_name='index',
            name='name',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
    ]

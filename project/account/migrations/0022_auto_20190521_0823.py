# Generated by Django 2.0 on 2019-05-21 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0021_auto_20190521_0732'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userregister',
            name='phone_number',
            field=models.CharField(help_text='Starts with +910', max_length=13),
        ),
    ]

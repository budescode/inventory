# Generated by Django 2.0 on 2019-12-10 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0024_cartitems_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitems',
            name='paid',
            field=models.BooleanField(default=True),
        ),
    ]
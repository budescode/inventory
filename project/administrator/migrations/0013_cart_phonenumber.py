# Generated by Django 2.0 on 2019-07-08 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0012_cart_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='phonenumber',
            field=models.TextField(default=''),
        ),
    ]
# Generated by Django 2.0 on 2019-12-09 23:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0020_cart_cartit'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartitems',
            old_name='product_id',
            new_name='cart_id',
        ),
    ]
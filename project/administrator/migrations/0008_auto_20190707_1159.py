# Generated by Django 2.0 on 2019-07-07 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0007_cart_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='product_id',
            new_name='category',
        ),
        migrations.AddField(
            model_name='cart',
            name='description',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
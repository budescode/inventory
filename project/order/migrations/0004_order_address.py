# Generated by Django 2.0 on 2019-11-15 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_remove_order_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='address',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]

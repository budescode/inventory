# Generated by Django 2.0 on 2019-12-17 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0025_cartitems_paid'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitems',
            name='paymentoption',
            field=models.CharField(blank=True, default='', max_length=20, null=True),
        ),
    ]

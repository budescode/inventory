# Generated by Django 2.0 on 2019-09-27 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0008_auto_20190927_0733'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='subcategory',
            field=models.CharField(default='', max_length=100),
        ),
    ]

# Generated by Django 2.0 on 2019-07-07 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0006_auto_20190707_1127'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='price',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
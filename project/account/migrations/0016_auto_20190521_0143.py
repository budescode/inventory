# Generated by Django 2.0 on 2019-05-21 00:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0015_auto_20190520_2334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sellercategory',
            name='select',
            field=models.CharField(blank=True, choices=[('Individual', 'Individual'), ('Agency', 'Agency')], max_length=30),
        ),
    ]
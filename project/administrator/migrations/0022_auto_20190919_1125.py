# Generated by Django 2.0 on 2019-09-19 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0021_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myitems',
            name='category',
            field=models.CharField(max_length=50),
        ),
    ]
# Generated by Django 2.0 on 2019-09-28 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0010_auto_20190928_0448'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='subcategory',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]

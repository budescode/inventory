# Generated by Django 2.0 on 2019-09-27 07:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0007_auto_20190927_0731'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myitems',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='myitemscategory', to='administrator.Category'),
        ),
    ]

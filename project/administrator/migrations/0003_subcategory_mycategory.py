# Generated by Django 2.0 on 2019-09-27 06:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0002_auto_20190926_0725'),
    ]

    operations = [
        migrations.AddField(
            model_name='subcategory',
            name='mycategory',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='mycategory', to='administrator.Category'),
        ),
    ]

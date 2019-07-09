# Generated by Django 2.0 on 2019-05-20 06:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('index', '0004_auto_20190520_0715'),
    ]

    operations = [
        migrations.AddField(
            model_name='poster',
            name='address',
            field=models.CharField(default='address', max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='poster',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]

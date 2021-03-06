# Generated by Django 2.0 on 2019-11-04 07:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.TextField()),
                ('phone_number', models.TextField()),
                ('order_id', models.TextField()),
                ('delivered', models.BooleanField(default=False)),
                ('paid', models.BooleanField(default=False)),
                ('paymentoption', models.CharField(blank=True, choices=[('Online', 'Online'), ('Delivery', 'Delivery'), ('Transfer', 'Transfer')], default='', max_length=20, null=True)),
                ('date', models.DateField(auto_now_add=True)),
                ('time', models.TimeField(auto_now_add=True)),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

# Generated by Django 2.0 on 2019-12-09 23:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0019_auto_20191210_0020'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='cartit',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cartitname', to='administrator.CartItems'),
        ),
    ]

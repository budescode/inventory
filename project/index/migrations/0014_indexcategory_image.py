# Generated by Django 2.0 on 2019-11-29 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0013_index_available'),
    ]

    operations = [
        migrations.AddField(
            model_name='indexcategory',
            name='image',
            field=models.FileField(default='', upload_to=''),
        ),
    ]

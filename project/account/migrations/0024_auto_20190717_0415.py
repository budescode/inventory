# Generated by Django 2.0 on 2019-07-17 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0023_changepassword_changepasswordcode_passwordresetemail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='brand',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='category',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
        migrations.AddField(
            model_name='profile',
            name='description',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='name',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='photo',
            field=models.FileField(default='', upload_to=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='title',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
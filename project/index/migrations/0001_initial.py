# Generated by Django 2.0 on 2019-11-04 07:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Index',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='index_images')),
                ('image1', models.ImageField(blank=True, null=True, upload_to='index_images')),
                ('image2', models.ImageField(blank=True, null=True, upload_to='index_images')),
                ('image3', models.ImageField(blank=True, null=True, upload_to='index_images')),
                ('image4', models.ImageField(blank=True, null=True, upload_to='index_images')),
                ('sex', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Unisex', 'Unisex')], max_length=10)),
                ('size', models.CharField(choices=[('S', 'S'), ('M', 'M'), ('L', 'L'), ('XL', 'XL'), ('2XL', '2XL'), ('3XL', '3XL'), ('4XL', '4XL')], max_length=10)),
                ('price', models.DecimalField(decimal_places=2, max_digits=20)),
                ('stock', models.IntegerField()),
                ('rating', models.PositiveIntegerField(blank=True, default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='IndexCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('unisex', models.CharField(choices=[('Men', 'Men'), ('Women', 'Women'), ('Boys', 'Boys'), ('Girls', 'Girls')], default='', max_length=10)),
                ('total_count', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='IndexSize',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='IndexSubCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('total_count', models.IntegerField(default=0)),
                ('mycategory', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='mycategory', to='index.IndexCategory')),
            ],
        ),
        migrations.AddField(
            model_name='index',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='index_category', to='index.IndexCategory'),
        ),
        migrations.AddField(
            model_name='index',
            name='subcategory',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='index_subcategory', to='index.IndexSubCategory'),
        ),
    ]

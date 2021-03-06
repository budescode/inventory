# Generated by Django 2.0 on 2019-09-26 07:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.TextField()),
                ('sex', models.TextField()),
                ('qty', models.IntegerField(default=1)),
                ('single_price', models.IntegerField(default=1)),
                ('price', models.IntegerField()),
                ('paid', models.BooleanField(default=False)),
                ('date', models.DateField()),
                ('size', models.CharField(max_length=10)),
                ('product_id', models.IntegerField(default=1)),
                ('paymentoption', models.CharField(blank=True, default='', max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='CountryDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('postcode', models.CharField(max_length=100)),
                ('suburb', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('dc', models.CharField(max_length=100)),
                ('detail_type', models.CharField(max_length=100)),
                ('lat', models.CharField(max_length=100)),
                ('ion', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='MyItems',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sex', models.TextField()),
                ('size', models.CharField(max_length=10)),
                ('price', models.DecimalField(decimal_places=2, max_digits=20)),
                ('stock', models.IntegerField()),
                ('category', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='mycategory', to='administrator.Category')),
            ],
        ),
        migrations.CreateModel(
            name='PettyCash',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('price', models.IntegerField()),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='myitems',
            name='subcategory',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='subcategory', to='administrator.SubCategory'),
        ),
    ]

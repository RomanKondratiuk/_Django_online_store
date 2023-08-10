# Generated by Django 4.2.4 on 2023-08-10 00:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='name ')),
                ('description', models.TextField(verbose_name='description')),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='name ')),
                ('description', models.TextField(verbose_name='description')),
                ('image', models.ImageField(blank=True, null=True, upload_to='image/', verbose_name='image')),
                ('category', models.TextField(verbose_name='category')),
                ('purchase_price', models.IntegerField()),
                ('date_of_creation', models.DateField()),
                ('last_modified_date', models.DateField()),
            ],
            options={
                'verbose_name': 'product',
                'verbose_name_plural': 'products',
                'ordering': ('name',),
            },
        ),
    ]

# Generated by Django 4.2.4 on 2023-08-27 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogpost', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='number_of_views',
            field=models.IntegerField(default=0, verbose_name='количество просмотров'),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='sign_publication',
            field=models.BooleanField(default=True, verbose_name='признак публикации'),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='slug',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='slug'),
        ),
    ]

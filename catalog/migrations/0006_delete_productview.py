# Generated by Django 4.2.4 on 2023-08-24 03:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_productview'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ProductView',
        ),
    ]
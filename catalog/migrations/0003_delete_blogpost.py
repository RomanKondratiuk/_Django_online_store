# Generated by Django 4.2.4 on 2023-08-23 01:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_blogpost'),
    ]

    operations = [
        migrations.DeleteModel(
            name='BlogPost',
        ),
    ]

# Generated by Django 3.1 on 2020-09-09 08:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20200909_0747'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='publish_date',
        ),
    ]

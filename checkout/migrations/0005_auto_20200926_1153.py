# Generated by Django 3.1 on 2020-09-26 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0004_auto_20200925_1942'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='gift_message',
            field=models.TextField(blank=True, default='', max_length=500),
        ),
    ]
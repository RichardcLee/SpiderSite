# Generated by Django 2.0.3 on 2018-04-26 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spider_site', '0009_auto_20180426_1318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='segmentfault',
            name='Author',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='segmentfault',
            name='Item',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='segmentfault',
            name='Tag',
            field=models.CharField(max_length=100),
        ),
    ]

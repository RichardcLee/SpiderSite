# Generated by Django 2.0.3 on 2018-05-29 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_site', '0006_auto_20180529_2134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='algorithmarticle',
            name='Title',
            field=models.CharField(max_length=40, primary_key=True),
        ),
    ]

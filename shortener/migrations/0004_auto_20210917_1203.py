# Generated by Django 3.1.7 on 2021-09-17 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0003_url_short_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='url',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]

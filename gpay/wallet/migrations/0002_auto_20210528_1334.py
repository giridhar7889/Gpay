# Generated by Django 3.1.1 on 2021-05-28 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wallet',
            name='user',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]

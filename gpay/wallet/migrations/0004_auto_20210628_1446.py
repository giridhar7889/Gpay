# Generated by Django 3.1.1 on 2021-06-28 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0003_auto_20210606_2257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wallet',
            name='wallet_name',
            field=models.CharField(default='wallet', max_length=100),
        ),
    ]

# Generated by Django 3.1.1 on 2021-06-06 17:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20210527_1922'),
        ('wallet', '0002_auto_20210528_1334'),
    ]

    operations = [
        migrations.AddField(
            model_name='wallet',
            name='wallet_name',
            field=models.CharField(default='wallet', max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='wallet',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='users.newuser'),
        ),
    ]

# Generated by Django 3.0.6 on 2020-05-09 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0002_auto_20200509_1229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='books',
            field=models.CharField(default=None, max_length=128),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='devlang',
            field=models.CharField(default=None, max_length=64),
        ),
    ]

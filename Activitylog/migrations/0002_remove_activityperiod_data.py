# Generated by Django 3.0.2 on 2020-03-29 11:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Activitylog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activityperiod',
            name='data',
        ),
    ]

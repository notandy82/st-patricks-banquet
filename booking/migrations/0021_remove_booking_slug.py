# Generated by Django 3.2.14 on 2022-08-04 14:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0020_booking_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='slug',
        ),
    ]

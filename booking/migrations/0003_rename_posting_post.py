# Generated by Django 3.2.14 on 2022-07-27 11:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0002_auto_20220725_1306'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Posting',
            new_name='Post',
        ),
    ]

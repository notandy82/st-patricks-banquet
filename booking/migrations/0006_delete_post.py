# Generated by Django 3.2.14 on 2022-07-27 13:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0005_post'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Post',
        ),
    ]
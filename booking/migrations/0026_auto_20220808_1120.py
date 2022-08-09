# Generated by Django 3.2.14 on 2022-08-08 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0025_delete_meal'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='adults',
            new_name='adult_meat',
        ),
        migrations.AddField(
            model_name='booking',
            name='adult_vegetarian',
            field=models.SmallIntegerField(default=0),
            preserve_default=False,
        ),
    ]
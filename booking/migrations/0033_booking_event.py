# Generated by Django 3.2.14 on 2022-08-11 14:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0032_remove_booking_event'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='event',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='booking.post'),
            preserve_default=False,
        ),
    ]

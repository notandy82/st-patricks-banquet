# Generated by Django 3.2.14 on 2022-08-11 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0029_alter_booking_additional_info'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='payment',
            field=models.CharField(choices=[('NP', 'Not Paid'), ('PA', 'Payment Accepted')], default='NP', max_length=12),
        ),
    ]

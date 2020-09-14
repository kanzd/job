# Generated by Django 3.1.1 on 2020-09-14 11:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('jobapi', '0004_bookings_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookings',
            name='Aloc',
            field=models.CharField(default='nono', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bookings',
            name='Bloc',
            field=models.CharField(default=django.utils.timezone.now, max_length=30),
            preserve_default=False,
        ),
    ]
# Generated by Django 3.1.1 on 2020-09-14 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobapi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='dob',
            field=models.DateTimeField(blank=True),
        ),
    ]

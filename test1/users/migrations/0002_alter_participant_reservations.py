# Generated by Django 4.2 on 2024-10-04 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conferences', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participant',
            name='reservations',
            field=models.ManyToManyField(related_name='Reservations', through='users.Reservation', to='conferences.conference'),
        ),
    ]

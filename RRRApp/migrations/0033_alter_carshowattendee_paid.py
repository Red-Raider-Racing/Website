# Generated by Django 4.2.3 on 2023-11-09 01:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RRRApp', '0032_carshowattendee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carshowattendee',
            name='paid',
            field=models.BooleanField(default=False, help_text='Check if the attendee has paid.'),
        ),
    ]

# Generated by Django 4.2.3 on 2023-11-06 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RRRApp', '0025_rename_carshowlocation_carshow'),
    ]

    operations = [
        migrations.AddField(
            model_name='carshow',
            name='email_preregister_payment_link',
            field=models.URLField(default=None, help_text='Enter the url to that will direct the user to the preregister payment.', max_length=500),
        ),
        migrations.AddField(
            model_name='carshow',
            name='email_subject',
            field=models.CharField(default=None, help_text='Enter the subject line of the email that will be send out to those who register for the car show. Ex: 2023 Red Raider Racing Car Show Registration', max_length=50),
        ),
    ]

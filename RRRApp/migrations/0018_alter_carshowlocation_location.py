# Generated by Django 4.2.3 on 2023-11-04 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RRRApp', '0017_alter_carshowlocation_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carshowlocation',
            name='location',
            field=models.CharField(help_text='Enter the the location of the car show in the format of an embedded HTML Google Map location. Tutorial on how to do this: <a href="https://support.google.com/maps/answer/144361?hl=en&co=GENIE.Platform%3DDesktop" target="_blank">Google Map</a>.', max_length=200),
        ),
    ]

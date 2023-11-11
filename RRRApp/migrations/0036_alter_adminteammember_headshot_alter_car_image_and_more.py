# Generated by Django 4.2.1 on 2023-11-10 23:31

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RRRApp', '0035_sponsor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adminteammember',
            name='headshot',
            field=models.ImageField(help_text='Upload a headshot image of the member in a 1x1 format.', storage=django.core.files.storage.FileSystemStorage(location='/media/adminMembers'), upload_to=''),
        ),
        migrations.AlterField(
            model_name='car',
            name='image',
            field=models.ImageField(help_text='Upload an image of the car.', storage=django.core.files.storage.FileSystemStorage(location='/media/cars'), upload_to=''),
        ),
        migrations.AlterField(
            model_name='merchitem',
            name='image',
            field=models.ImageField(help_text='Upload the image of the merch item. Preferably a .png file with no background.', storage=django.core.files.storage.FileSystemStorage(location='/media/merchItems'), upload_to=''),
        ),
        migrations.AlterField(
            model_name='merchitem',
            name='secondary_image',
            field=models.ImageField(blank=True, help_text='Upload the secondary image of the merch item. This could be the back of the shirt. Preferably a .png file with no background. (Optional)', null=True, storage=django.core.files.storage.FileSystemStorage(location='/media/merchItems'), upload_to=''),
        ),
        migrations.AlterField(
            model_name='sponsor',
            name='sponsor_logo',
            field=models.ImageField(help_text='Upload an image of the sponsors logo. Make sure the background is either transparent or white. ', storage=django.core.files.storage.FileSystemStorage(location='/media/sponsors'), upload_to=''),
        ),
        migrations.AlterField(
            model_name='techincalteammember',
            name='headshot',
            field=models.ImageField(help_text='Upload a headshot image of the member in a 1x1 format.', storage=django.core.files.storage.FileSystemStorage(location='/media/technicalMembers'), upload_to=''),
        ),
    ]

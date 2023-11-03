# Generated by Django 4.2.3 on 2023-11-03 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RRRApp', '0004_adminmember_techincalmember_delete_member'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adminmember',
            name='headshot',
            field=models.FileField(upload_to='adminMembers/'),
        ),
        migrations.AlterField(
            model_name='car',
            name='image',
            field=models.FileField(upload_to='cars/'),
        ),
        migrations.AlterField(
            model_name='merchitem',
            name='image',
            field=models.FileField(upload_to='merchItems/'),
        ),
        migrations.AlterField(
            model_name='techincalmember',
            name='headshot',
            field=models.FileField(upload_to='technicalMembers/'),
        ),
    ]
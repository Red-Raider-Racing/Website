# Generated by Django 4.2.3 on 2023-11-09 01:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RRRApp', '0031_carshow_location_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarShowAttendee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(help_text="Enter the attendee's first name.", max_length=200)),
                ('last_name', models.CharField(help_text="Enter the attendee's last name.", max_length=200)),
                ('email', models.CharField(help_text="Enter the attendee's email.", max_length=200)),
                ('section', models.CharField(help_text="Enter the attendee's section.", max_length=200)),
                ('paid', models.BooleanField(help_text='Check if the attendee has paid.')),
            ],
        ),
    ]

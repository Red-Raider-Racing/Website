# Generated by Django 4.2.3 on 2023-11-03 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RRRApp', '0003_alter_car_image_alter_member_headshot_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdminMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headshot', models.FileField(upload_to='uploads/adminMembers/')),
                ('name', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('linkedIn', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='TechincalMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headshot', models.FileField(upload_to='uploads/technicalMembers/')),
                ('name', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('linkedIn', models.URLField()),
            ],
        ),
        migrations.DeleteModel(
            name='Member',
        ),
    ]

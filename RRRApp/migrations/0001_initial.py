# Generated by Django 4.2.3 on 2023-11-03 18:01

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image', models.URLField()),
                ('chassis', models.CharField(max_length=200)),
                ('power_unit', models.CharField(max_length=200)),
                ('weight', models.CharField(max_length=200)),
                ('main_achievement', models.CharField(max_length=200)),
                ('competition_placement', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headshot', models.URLField()),
                ('name', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('linkedIn', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='MerchItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.URLField()),
                ('item_name', models.CharField(max_length=200)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(9999.99)])),
                ('size', models.BooleanField()),
            ],
        ),
    ]

# Generated by Django 4.2.3 on 2023-11-04 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RRRApp', '0015_alter_merchitem_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarShowLocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField(help_text='Enter the year of the car show in the format YYYY. Ex: 2023.')),
                ('location', models.CharField(help_text='Enter the the location of the car show in the format of an embedded HTML Google Map location. Ex: <iframe src="https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d13309.266909665284!2d-101.8471117!3d33.4931358!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x86fe6e7f789c8511%3A0xbbd67681ff2d290!2sCooks%20Garage!5e0!3m2!1sen!2sus!4v1698369768727!5m2!1sen!2sus" width="600" height="450" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade" title="2023-24 Car Show Location"></iframe>. Tutorial on how to do this: https://support.google.com/maps/answer/144361?hl=en&co=GENIE.Platform%3DDesktop.', max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='merchitem',
            name='size',
            field=models.BooleanField(help_text='Toggle on if a size section should be included. Ex: Shirts'),
        ),
    ]

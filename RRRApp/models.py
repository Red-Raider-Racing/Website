from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class MerchItem(models.Model):
    image = models.FileField(upload_to='merchItems/', help_text="Upload the image of the merch item. Preferably a .png file with no background.")
    item_name = models.CharField(max_length=200, help_text="Enter the item's name. Do not include an underscore ('_') in the name.")
    price = models.DecimalField(
            max_digits=6, decimal_places=2,
            validators=[MinValueValidator(0.00), MaxValueValidator(9999.99)],
            help_text="Enter the item's price."
        )  # Maximum cost set to 9999 with 2 decimal places
    size = models.BooleanField(help_text="Toggle on if a size section should be included. Ex: Shirts")

    def __str__(self) -> str:
        return self.item_name

class AdminTeamMember(models.Model):
    headshot = models.FileField(upload_to='adminMembers/', help_text="Upload a headshot image of the member in a 1x1 format.")
    member_name = models.CharField(max_length=200, help_text="Enter the member's name.")
    title = models.CharField(max_length=200, help_text="Enter the member's title.")
    school_email = models.EmailField(max_length=200, help_text="Enter the member's school email address.")
    linkedIn = models.URLField(max_length=200, help_text="Enter the member's LinkedIn profile URL. (Optional)", blank=True, null=True)

    def __str__(self) -> str:
        return self.member_name
    
class TechincalTeamMember(models.Model):
    headshot = models.FileField(upload_to='technicalMembers/', help_text="Upload a headshot image of the member in a 1x1 format." )
    member_name = models.CharField(max_length=200, help_text="Enter the member's name.")
    title = models.CharField(max_length=200, help_text="Enter the member's title.")
    school_email = models.EmailField(max_length=200, help_text="Enter the member's school email address.")
    linkedIn = models.URLField(max_length=200, help_text="Enter the member's LinkedIn profile URL. (Optional)", blank=True, null=True)

    def __str__(self) -> str:
        return self.member_name

class Car(models.Model):
    car_name = models.CharField(max_length=50, help_text="Enter the name of the car in the format: RRR-YYYY. Ex: RRR-2023.")
    image = models.FileField(upload_to='cars/', help_text="Upload an image of the car.")
    chassis = models.CharField(max_length=200, help_text="Enter the chassis details of the car. (Optional)", blank=True, null=True)
    power_unit = models.CharField(max_length=200, help_text="Enter the power unit details of the car. (Optional)", blank=True, null=True)
    weight = models.IntegerField(help_text="Enter the weight of the car. (Optional)",blank=True,null=True)
    main_achievement = models.TextField(max_length=200, help_text="Enter the car's main achievement. (Optional)", blank=True)
    competition_placement = models.CharField(max_length=200, help_text="Enter the car's competition placement. Format: placement/# of teams. Ex: 50/120. (Optional)", blank=True)

    def __str__(self) -> str:
        return self.car_name
    
class CarShowLocation(models.Model):
    year = models.IntegerField(help_text="Enter the year of the car show in the format YYYY. Ex: 2023.")
    date = models.DateField(help_text="Enter the date the car show will take place.", default=None, null=True, blank=True)
    start_time = models.CharField(max_length=8,help_text="Enter the time the car show will start. Format: TT:TT AM. Ex: 9:00 AM", default=None, null=True, blank=True)
    end_time = models.CharField(max_length=8,help_text="Enter the time the car show will end. Format: TT:TT PM. Ex: 9:00 PM", default=None, null=True, blank=True)
    location = models.TextField(max_length=2000, help_text='Enter the location of the car show in the format of an embedded HTML Google Map location. Tutorial on how to do this: <a href="https://support.google.com/maps/answer/144361?hl=en&co=GENIE.Platform%3DDesktop" target="_blank">Google Map</a>.')

    def __str__(self) -> str:
        return str(self.year)
    
class FAQQuestion(models.Model):
    question = models.CharField(max_length=200,help_text="Enter the frequently asked question.")
    answer = models.TextField(max_length=2000, help_text='Enter the answer to the FAQ.')

    def __str__(self) -> str:
        return self.question


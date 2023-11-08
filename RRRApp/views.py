from django.shortcuts import render, redirect
from .functions.email import emailMessage, formatMessage, carShowEmailFormat
from .functions.merch import merchMessageFormat
from .functions.carShowReg import insertRow
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.cache import cache_page
from RRRWebsite.settings import CACHE_TIMEOUT
from .models import *

mainEmail = 'redraiderracingcode@outlook.com' # When testing

TEMPLATE_DIRS = (
    'os.path.join(BASE_DIR, "templates"),'
)

#----------------Pages----------------

def load(request):
    '''
    Puts the user onto the homepage when initially visiting the website.
    '''
    return redirect("/home/")

@cache_page(CACHE_TIMEOUT)
@csrf_exempt
def index(request):
    merch_items = MerchItem.objects.all()
    if request.method == 'GET':
        return render(request, "index.html", {"merch": merch_items})
    else:
        # Handle the form data here
        name = request.POST.get('name')
        email = request.POST.get('email')

        subject = request.POST.get('subject')
        if subject:
            message = request.POST.get('message')

            try:
                # Perform any backend processing (e.g., saving to the database)
                message = formatMessage(name,email,subject,message)
                emailMessage(subject, message, 'redraiderracing@website.admin', mainEmail)

                # Set success message
                success = 1
            except Exception as e:
                # Set error message
                success = 0

            # Render the template with the success or error message
            return redirect(f"/home/?success={success}")
        else:
            sizeItem = request.POST.get('item')
            if '_' not in sizeItem:
                size = None
                item = sizeItem
            else:
                size = sizeItem.split('_')[0]
                item = sizeItem.split('_')[1]
            merch_item = merch_items.get(item_name=item)
            item_num = merch_item.id - 1
            try:
                # Perform any backend processing (e.g., saving to the database)
                message = merchMessageFormat(name, item, size)
                message = formatMessage('Website Merch Manager', email, subject, message)
                emailMessage(f'{item} Availability', message, 'redraiderracing@website.admin', mainEmail)

                # Set success message
                success = 1
            except Exception as e:
                # Set error message
                success = 0

            # Render the template with the success or error message
            return redirect(f'/home/?success={success}&item={item_num}')

@cache_page(CACHE_TIMEOUT)
def team(request):
    adminMembers = AdminTeamMember.objects.all()
    technicalMembers = TechincalTeamMember.objects.all()

    main_data = {
        "adminMembers":adminMembers,
        "technicalMembers":technicalMembers
    }
    return render(request, "team.html", main_data)

@cache_page(CACHE_TIMEOUT)
def cars(request):
    car_items = Car.objects.all().order_by('-id')
    return render(request, "cars.html", {"cars": car_items})

@cache_page(CACHE_TIMEOUT)
def sponsor(request):
    return render(request, "sponsor.html",)

@cache_page(CACHE_TIMEOUT)
@csrf_exempt
def carshow(request):
    carShowLoc = CarShow.objects.last()
    if request.method == 'GET':
        return render(request, "carshow.html", {"location": carShowLoc})
    else:
        # Handle the form data here
        firstName = request.POST.get('first_name')
        lastName = request.POST.get('last_name')
        email = request.POST.get('email')
        section = request.POST.get('car_type')

        try:
            # Perform any backend processing (e.g., saving to the database)
            insertRow(firstName, lastName, email, section)
            message = carShowEmailFormat(firstName, lastName, email, section, carShowLoc, mainEmail)
            emailMessage(f"{carShowLoc.year} Red Raider Racing Car Show Registration", message, mainEmail, email)

            # Set success message
            success = 1
        except Exception as e:
            # Set error message
            success = 0

        # Render the template with the success or error message
        return redirect(f"/car-show/?success={success}#message-container")

@cache_page(CACHE_TIMEOUT)
def faq(request):
    questions = FAQQuestion.objects.all()
    return render(request, "faq.html", {"questions": questions})

@cache_page(CACHE_TIMEOUT)
def privacy(request):
    return render(request, "privacy.html",)

@cache_page(CACHE_TIMEOUT)
def terms(request):
    return render(request, "terms.html",)

@cache_page(CACHE_TIMEOUT)
def custom_404(request):
    return render(request, '404.html', status=404)

@cache_page(CACHE_TIMEOUT)
def custom_500(request):
    return render(request, '500.html', status=500)


#----------------Robots----------------

def robots(request):
    return render(request, "robots.txt",)
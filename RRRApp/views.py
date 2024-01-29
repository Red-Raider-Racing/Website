from django.shortcuts import render, redirect
from .functions.email import emailMessage, formatMessage, carShowEmailFormat
from .functions.merch import merchMessageFormat
from .functions.carShowReg import insertRow
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.cache import cache_page
from RRRWebsite.settings import CACHE_TIMEOUT
from .models import *
from itertools import chain
from django.http import HttpResponse
import logging
logging.basicConfig(level=logging.INFO)

mainEmail = 'formulasaettu@gmail.com'
websiteEmail = 'redraiderracing@website.admin'

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
    merch_items = MerchItem.objects.all().order_by('-item_name')
    if request.method == 'GET':
        return render(request, "index.html", {"merch": merch_items})
    elif request.method == 'POST':
        # Handle the form data here
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        honeypot = request.POST.get('human_verification')

        if honeypot:
            logging.error("Bot filled out form")
            response = HttpResponse("Bot Detected", status=400)
            response['Location'] = '/home/'
            return response

        if subject:
            message = request.POST.get('message')

            try:
                # Perform any backend processing (e.g., saving to the database)
                message = formatMessage(name,email,subject,message)
                emailMessage(subject, message, websiteEmail, mainEmail)

                # Set success message
                success = 1
            except Exception as e:
                logging.error("An error occurred: %s", e)
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
                emailMessage(f'{item} Availability', message, websiteEmail, mainEmail)

                # Set success message
                success = 1
            except Exception as e:
                logging.error("An error occurred: %s", e)
                # Set error message
                success = 0

            # Render the template with the success or error message
            return redirect(f'/home/?success={success}&item={item_num}')
    else:
        return HttpResponse('Method not allowed')

@cache_page(CACHE_TIMEOUT)
def team(request):
    adminFirst = AdminTeamMember.objects.filter(first=True).order_by('sub_section', 'member_name')
    adminOther = AdminTeamMember.objects.filter(first=False).order_by('sub_section', 'member_name')
    adminMembers = list(chain(adminFirst, adminOther))

    techFirst = TechincalTeamMember.objects.filter(first=True).order_by('sub_section', 'member_name')
    techOther = TechincalTeamMember.objects.filter(first=False).order_by('sub_section', 'member_name')
    technicalMembers = list(chain(techFirst, techOther))

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
    sponsors = Sponsor.objects.all().order_by('sponsor_name')
    return render(request, "sponsor.html", {"sponsors": sponsors})

@cache_page(CACHE_TIMEOUT)
@csrf_exempt
def carshow(request):
    carShowLoc = CarShow.objects.last()
    if request.method == 'GET':
        return render(request, "carshow.html", {"location": carShowLoc})
    elif request.method == 'POST':
        logging.info("Received form data: %s", request.POST)
        # Handle the form data here
        firstName = request.POST.get('first_name')
        lastName = request.POST.get('last_name')
        email = request.POST.get('email')
        section = request.POST.get('car_type')
        honeypot = request.POST.get('human_verification')

        if honeypot:
            logging.error("Bot filled out form")
            response = HttpResponse("Bot Detected", status=400)
            response['Location'] = '/car-show/?success=0#message-container'
            return response

        try:
            # Perform any backend processing (e.g., saving to the database)
            attendee = CarShowAttendee(first_name=firstName.capitalize(),last_name=lastName.capitalize(),email=email,section=section.capitalize())
            attendee.save()
            insertRow(firstName, lastName, email, section)
            message = carShowEmailFormat(firstName, lastName, email, section, carShowLoc, mainEmail)
            emailMessage(f"{carShowLoc.year} Red Raider Racing Car Show Registration", message, mainEmail, email)

            # Set success message
            success = 1
        except Exception as e:
            logging.error("An error occurred: %s", e)
            # Set error message
            success = 0

        # Render the template with the success or error message
        return redirect(f"/car-show/?success={success}#message-container")
    else:
        return HttpResponse('Method not allowed')

@cache_page(CACHE_TIMEOUT)
def faq(request):
    firstQuestions = FAQQuestion.objects.filter(first=True).order_by('id')
    otherQuestions = FAQQuestion.objects.filter(first=False).order_by('id')
    questions = list(chain(firstQuestions, otherQuestions))

    return render(request, "faq.html", {"questions": questions})

@cache_page(CACHE_TIMEOUT)
def privacy(request):
    return render(request, "privacy.html",)

@cache_page(CACHE_TIMEOUT)
def terms(request):
    return render(request, "terms.html",)

@cache_page(CACHE_TIMEOUT)
def custom_404(request):
    if request.method == 'GET':
        return render(request, '404.html', status=404)
    elif request.method == 'POST':
        # Handle the form data here
        name = request.POST.get('name')
        email = request.POST.get('email')

        subject = request.POST.get('subject')
        message = request.POST.get('message')
        honeypot = request.POST.get('human_verification')

        if honeypot:
            logging.error("Bot filled out form")
            response = HttpResponse("Bot Detected", status=400)
            response['Location'] = '/404/?success=0'
            return response

        try:
            # Perform any backend processing (e.g., saving to the database)
            message = formatMessage(name,email,subject,message)
            emailMessage(f'Sent From 404 Page: {subject}', message, websiteEmail, mainEmail)

            # Set success message
            success = 1
        except Exception as e:
            logging.error("An error occurred: %s", e)
            # Set error message
            success = 0

        # Render the template with the success or error message
        return redirect(f"/404/?success={success}")
    else:
        return HttpResponse('Method not allowed')
    

@cache_page(CACHE_TIMEOUT)
def custom_500(request):
    try:
        emailMessage('Major Website Error','An internal server error happened on the website. Please look into this error.', websiteEmail, mainEmail)
    except Exception as e:
        print(e)
        logging.error("An error occurred when sending the error email: %s", e)
    return render(request, '500.html', status=500)


#----------------Robots----------------

def robots(request):
    return render(request, "robots.txt",)
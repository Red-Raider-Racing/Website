from django.shortcuts import render, redirect
from .functions.email import emailMessage
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.cache import cache_page
from RRRWebsite.settings import CACHE_TIMEOUT

TEMPLATE_DIRS = (
    'os.path.join(BASE_DIR, "templates"),'
)

#----------------Pages----------------
# Just puts the user onto the homepage when initially visiting the website
def load(request):
    return redirect(f"/home/")

@cache_page(CACHE_TIMEOUT)
@csrf_exempt
def index(request):
    if request.method == 'GET':
        return render(request, "index.html")
    else:
        # Handle the form data here
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        try:
            # Perform any backend processing (e.g., saving to the database)
            '''call formatting functions here'''
            emailMessage(name, email, subject, message)

            # Set success message
            success = 1
        except Exception as e:
            # Handle the error case
            # You can log the error for debugging
            print(f"Error: {str(e)}")

            # Set error message
            success = 0

        # Render the template with the success or error message
        return redirect(f"/home/?success={success}#message")

@cache_page(CACHE_TIMEOUT)
def team(request):
    return render(request, "team.html",)

@cache_page(CACHE_TIMEOUT)
def cars(request):
    return render(request, "cars.html",)

@cache_page(CACHE_TIMEOUT)
def sponsor(request):
    return render(request, "sponsor.html",)

@cache_page(CACHE_TIMEOUT)
def carshow(request):
    return render(request, "carshow.html",)

@cache_page(CACHE_TIMEOUT)
def faq(request):
    return render(request, "faq.html",)

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
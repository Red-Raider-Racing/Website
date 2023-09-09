from django.shortcuts import render
from django.http import HttpResponse

from django.views.decorators.csrf import csrf_exempt

TEMPLATE_DIRS = (
    'os.path.join(BASE_DIR, "templates"),'
)

#----------------Pages----------------
def index(request):
    return render(request, "index.html",)

def team(request):
    return render(request, "team.html",)

def cars(request):
    return render(request, "cars.html",)

def sponsor(request):
    return render(request, "sponsor.html",)

def carshow(request):
    return render(request, "carshow.html",)

def faq(request):
    return render(request, "faq.html",)

#----------------Responses----------------

def submit_contact(request):
    if request.method == 'POST':
        # Handle the form data here
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Perform any backend processing (e.g., saving to the database)
        '''call functions here'''
        print(f"name: {name}\nemail: {email}\nsubject: {subject}\nmessage: {message}\n")

        # You can also return a response or redirect to another page
        return render(request, 'index.html')

    # Handle other HTTP methods or display a form initially
    return render(request, 'index.html')
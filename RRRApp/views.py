from django.shortcuts import render
from .functions.email import emailMessage
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseServerError

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

def custom_404(request, exception):
    return render(request, '404.html', status=404)

def custom_500(request):
    return render(request, '500.html', status=500)

#----------------Responses----------------

@csrf_exempt
async def submit_contact(request):
    if request.method == 'POST':
        # Handle the form data here
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Perform any backend processing (e.g., saving to the database)
        '''call formatting functions here'''
        print(f"name: {name}\nemail: {email}\nsubject: {subject}\nmessage: {message}\n")
        
        # Await asynchronous email sending and catch exceptions
        try:
            await emailMessage(name, email, subject, message)
        except Exception as e:
            # Render the 500.html error page with the exception information
            return HttpResponseServerError(render(request, '500.html', context={'exception': str(e)}))

        # Return a success response
        return HttpResponse('Email sent successfully')

    # Handle other HTTP methods or display a form initially
    return render(request, 'index.html')
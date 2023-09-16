from django.shortcuts import render, redirect
from .functions.email import emailMessage
from django.views.decorators.csrf import csrf_exempt

TEMPLATE_DIRS = (
    'os.path.join(BASE_DIR, "templates"),'
)

#----------------Pages----------------
def load(request):
    return redirect(f"/home/")

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

def custom_404(request):
    return render(request, '404.html', status=404)

def custom_500(request):
    return render(request, '500.html', status=500)

#----------------Responses----------------

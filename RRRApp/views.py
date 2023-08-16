from django.shortcuts import render
from django.http import JsonResponse
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
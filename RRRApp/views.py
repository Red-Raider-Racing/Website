from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

TEMPLATE_DIRS = (
    'os.path.join(BASE_DIR, "templates"),'
)

def index(request):
    return render(request, "index.html",)
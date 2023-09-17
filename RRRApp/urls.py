from django.urls import path
from . import views
from django.views.static import serve
from django.http import HttpResponse

def custom_serve(request, path, document_root=None, show_indexes=False):
    response = serve(request, path, document_root, show_indexes)
    response['Cache-Control'] = 'max-age=86400'  # Set cache control header to cache for 24 hours (86400 seconds)
    return response

urlpatterns = [
    #----------------Pages----------------
    path('',views.load, name='home'),
    path('home/',views.index, name='home'),
    path('team/',views.team, name='team'),
    path('cars/',views.cars, name='cars'),
    path('sponsors/',views.sponsor, name='sponsor'),
    path('car-show/',views.carshow, name='carshow'),
    path('faq/',views.faq, name='faq'),

    #----------------Error Pages----------------
    path('404/',views.custom_404, name='404'),
    path('500/',views.custom_500, name='500'),
    
    #----------------Cache----------------
    path('static/<path:path>', custom_serve),
]
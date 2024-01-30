from django.urls import path
from . import views
from django.views.static import serve
from django.views.generic.base import RedirectView

def custom_serve(request, path, document_root=None, show_indexes=False):
    response = serve(request, path, document_root, show_indexes)
    response['Cache-Control'] = 'max-age=86400'  # Set cache control header to cache for 24 hours (86400 seconds)
    return response

urlpatterns = [
    #----------------Old Google Pages----------------
    path('registration/',views.registration, name='registration'),

    #----------------Pages----------------
    path('',views.load, name='home'),
    path('home/',views.index, name='home'),
    path('team/',views.team, name='team'),
    path('cars/',views.cars, name='cars'),
    path('sponsors/',views.sponsor, name='sponsor'),
    path('car-show/',views.carshow, name='carshow'),
    path('faq/',views.faq, name='faq'),
    path('privacy-policy/',views.privacy, name='privacy'),
    path('terms-of-service/',views.terms, name='terms'),

    #----------------Error Pages----------------
    path('404/',views.custom_404, name='404'),
    path('500/',views.custom_500, name='500'),  # possibly change this back to path('500/',views.custom_500, name='500')
    
    #----------------Cache----------------
    path('static/<path:path>', custom_serve),

    #----------------Robots----------------
    path('robots.txt/', views.robots, name='robots'), # this makes is so crawlers can use our website (SEO)

    #----------------Favicon----------------
    path('favicon.ico', RedirectView.as_view(url='/static/logos/favicon.ico')),
]
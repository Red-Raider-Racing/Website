from django.urls import path
from . import views
import asyncio

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
    
    #----------------requests----------------
]
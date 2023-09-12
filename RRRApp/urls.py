from django.urls import path
from . import views
import asyncio

urlpatterns = [
    #----------------Pages----------------
    path('',views.index, name='home'),
    path('home/',views.index, name='home'),
    path('team/',views.team, name='team'),
    path('cars/',views.cars, name='cars'),
    path('sponsors/',views.sponsor, name='sponsor'),
    path('car-show/',views.carshow, name='carshow'),
    path('faq/',views.faq, name='faq'),
    
    #----------------requests----------------
    path('submit_contact/', views.submit_contact, name='submit_contact'),
]
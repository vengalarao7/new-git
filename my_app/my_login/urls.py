# from django.contrib import admin
from django.urls import path
from .views import registration, registration_success


urlpatterns = [
     path('registration/', registration, name='registration'),
     path('registration/success/', registration_success, name='registration_success'),
]
from django.contrib import admin
from django.urls import path
from django.contrib import admin
from HOME import views

urlpatterns = [
    path("",views.index, name='HOME'),
    path("about",views.about, name='about'),
    path("services",views.services, name='services'),
    path("contactUs",views.contactUs, name='contactUs'),
    
]